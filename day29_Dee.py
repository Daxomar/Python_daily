import os
from datetime import datetime, timezone

from bson import ObjectId
from bson.errors import InvalidId
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017"))
collection = client[os.environ.get("MONGODB_DATABASE", "thirty_days_of_python")]["students"]


def serialize(student):
	student["_id"] = str(student["_id"])
	if isinstance(student.get("created_at"), datetime):
		student["created_at"] = student["created_at"].isoformat()
	return student


def payload():
	data = request.get_json(silent=True) or request.form.to_dict()
	skills = data.get("skills", [])
	if isinstance(skills, str):
		skills = [skill.strip() for skill in skills.split(",") if skill.strip()]
	return {
		"name": data.get("name", "").strip(),
		"country": data.get("country", "").strip(),
		"city": data.get("city", "").strip(),
		"birthyear": data.get("birthyear"),
		"skills": skills,
		"bio": data.get("bio", "").strip(),
	}


def object_id(value):
	try:
		return ObjectId(value)
	except (InvalidId, TypeError):
		return None


@app.get("/api/v1.0/students")
def students():
	return jsonify([serialize(student) for student in collection.find()])


@app.get("/api/v1.0/students/<student_id>")
def student(student_id):
	identifier = object_id(student_id)
	if identifier is None:
		return jsonify({"error": "invalid id"}), 400
	result = collection.find_one({"_id": identifier})
	if result is None:
		return jsonify({"error": "student not found"}), 404
	return jsonify(serialize(result))


@app.post("/api/v1.0/students")
def create_student():
	data = payload()
	if not data["name"]:
		return jsonify({"error": "name is required"}), 400
	data["created_at"] = datetime.now(timezone.utc)
	result = collection.insert_one(data)
	data["_id"] = result.inserted_id
	return jsonify(serialize(data)), 201


@app.put("/api/v1.0/students/<student_id>")
def update_student(student_id):
	identifier = object_id(student_id)
	if identifier is None:
		return jsonify({"error": "invalid id"}), 400
	data = payload()
	result = collection.update_one({"_id": identifier}, {"$set": data})
	if result.matched_count == 0:
		return jsonify({"error": "student not found"}), 404
	return jsonify(serialize(collection.find_one({"_id": identifier})))


@app.delete("/api/v1.0/students/<student_id>")
def delete_student(student_id):
	identifier = object_id(student_id)
	if identifier is None:
		return jsonify({"error": "invalid id"}), 400
	result = collection.delete_one({"_id": identifier})
	if result.deleted_count == 0:
		return jsonify({"error": "student not found"}), 404
	return "", 204


if __name__ == "__main__":
	app.run(
		host="0.0.0.0",
		port=int(os.environ.get("PORT", 5000)),
		debug=os.environ.get("FLASK_DEBUG", "0") == "1",
	)
