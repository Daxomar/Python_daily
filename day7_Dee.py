# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Length of the set it_companies:", len(it_companies))
it_companies.add("Twitter")
print("After adding Twitter:", it_companies)
it_companies.update(["LinkedIn", "Snapchat"])
print("After adding LinkedIn and Snapchat:", it_companies)
it_companies.remove("IBM")
print("After removing IBM:", it_companies)
print("The difference between remove and discard is that remove will raise a KeyError if the item does not exist in the set, while discard will not raise an error.")

print("Union of A and B:", A.union(B))
print("Intersection of A and B:", A.intersection(B))
if A.issubset(B):
    print("A is a subset of B")

if A.isdisjoint(B):
    print("A and B have no elements in common")

print("Symmetric difference between A and B:", A.symmetric_difference(B))
print("Deleting the sets A and B")
del A,B
age_set = set(age)
print("Length of the age set:", len(age_set))
print("The length of the age list: ", len(age), "The length of the age set: ", len(age_set))
print("A string is define as a sequence of characters.\n A set is a collection of unique elements.\n A list is an ordered collection of elements that can contain duplicates.\n A tuple is an ordered collection of elements that cannot be changed (immutable).")
string = "I am a teacher and I love to inspire and teach people"
words = string.split()
print("Unique words in the string:", len(set(words)))