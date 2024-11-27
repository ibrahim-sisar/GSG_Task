import os
import datetime
import cs50
import json

current_date = datetime.datetime.now()
CurrentYear = int(current_date.year)


last_name = cs50.get_string("last name: ")
file_source = f"{last_name}.json"




if os.path.exists(file_source):

   opend_file = open(file_source)
   data = json.load(opend_file)
   id_number = data['ID_Number']
   first_name = data['First_Name']
   age = data['Age']
   mobile_number=data['Mobile_Number']
   email_address = data['Email_Address']

   print(first_name)



   if age < 18:
      print("child")
   elif age <= 39:
     print("adult")
   elif age <= 59:
     print("Middle Age Adult")
   else:
     print("Senior Adult")


   if mobile_number[:3] == "059":
      print("JAWWAL")
   elif mobile_number[:3] == "056":
      print("OREDDO")
   else:
      print(f"your sim provider comapny code : {mobile_number[:3]} is not palestinian  ")


   email_domain = email_address.split("@")[1]
   print(f"your domain for your email is : {email_domain}")


   opend_file.close()

else:
   id_number = cs50.get_int("id number: ")
   first_name  = cs50.get_string("first name: ")
   YearOfBirth = cs50.get_int("Year Of Birth: ")
   myAge = CurrentYear - YearOfBirth
   mobile_number = cs50.get_string("mobile number: ")
   email_address = cs50.get_string("email address: ")
   
   data = {
      "ID_Number": id_number,
      "First_Name": first_name,
      "Last_Name": last_name,
      "Age": myAge,
      "Mobile_Number": mobile_number,
      "Email_Address": email_address
   }
   
   with open(file_source, 'w') as outfile:
      json.dump(data, outfile)










