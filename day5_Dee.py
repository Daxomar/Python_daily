smplst = ['Orange', 'Mango','lemon']
smplst5 = ['Apple', 'Banana', 'Grapes', 'Pineapple', 'Strawberry', 'Watermelon', 'Papaya', 'Kiwi', 'Cherry', 'Peach']
print("The original list is : " + str(smplst))
print("The first item of list is : " + str(smplst[0]))
print("The last item of list is : " + str(smplst[-1]))
mixed_data_types = ["Dee",250,6.5,True,"Nii kaks"]
print("The mixed data types list is : " + str(mixed_data_types))
it_company = ["Google", "Microsoft", "Apple", "Facebook"]
print("The IT company list is : " + str(it_company))
print("The number of companies in the list is : " + str(len(it_company)))
print("The first company in the list is : " + str(it_company[0]))
print("The last company in the list is : " + str(it_company[-1]))
print("This is how the list looks after adding a new company : " + str(it_company.append("Amazon")))
print("The list after adding something to the middle is : " + str(it_company.insert(2, "Twitter")))    
print("I have made all the companies in the list uppercase : " + str([i.upper() for i in it_company]))
print("I have join the companies in the list with a '#' : " + str('#'.join(it_company)))
print("Checking if a company is in the list or not : " + str("Google" in it_company))
print("Sorting the list in ascending order : " + str(sorted(it_company)))
print("Reversing the list : " + str(it_company.reverse()))
print("Slicing the list to get the first three companies : " + str(it_company[0:3]))
print("Slicing the list to get the last three companies : " + str(it_company[-3:]))
print("Slicing the list to get the middle companies : " + str(it_company[1:3]))
print("Removing the first company from the list : " + str(it_company.remove(it_company[0])))
print("Removing the last company from the list : " + str(it_company.pop()))
print("Removing a company from the middle of the list : " + str(it_company.pop(1)))
print("Removing all companies from the list : " + str(it_company.clear()))
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node","Express", "MongoDB"]
full_stack = front_end + back_end
print("The full stack is : " + str(full_stack))
print("inserting Python and SQL after Redux in the full stack list : " + str(full_stack.insert(5, "Python")))
print("inserting SQL after Python in the full stack list : " + str(full_stack.insert(6, "SQL")))

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("The ages list is : " + str(ages))
print("The minimum age is : " + str(min(ages)))
print("The maximum age is : " + str(max(ages)))
ages.sort()
print("The sorted ages list is : " + str(ages))
print ("Adding the minimum age and maximum age to the list : " + str(ages.append(min(ages))) + " and " + str(ages.append(max(ages))))
print ("The median age is : " + str((ages[len(ages)//2] + ages[(len(ages)-1)//2]) / 2))
print ("The average age is : " + str(sum(ages)/len(ages)))
print ("The range of the ages is : " + str(max(ages) - min(ages)))
print("Comparing the value of (min - average) and (max - average) : " + str(abs(min(ages) - (sum(ages)/len(ages)))) + " and " + str(abs(max(ages) - (sum(ages)/len(ages)))))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
print("The middle country/countries in the list is/are : " + str(countries[len(countries)//2]) + " and " + str(countries[(len(countries)-1)//2]))
print("Dividing the countries list into two equal lists : " + str(countries[:len(countries)//2]) + " and " + str(countries[len(countries )//2:]))
