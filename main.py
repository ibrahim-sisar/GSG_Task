import os
import datetime
import cs50

current_date = datetime.datetime.now()
CurrentYear = int(current_date.year)


last_name = cs50.get_string("last name: ")
file_source = f"{last_name}.txt"




if os.path.exists(file_source):

   opend_file = open(file_source)

   opend_file_to_list = [i.strip() for i in opend_file.readlines() ]

   first_name = opend_file_to_list[1].split(":")[1].strip()
   last_name = opend_file_to_list[2].split(":")[1].strip()
   id_number = opend_file_to_list[0].split(":")[1].strip()
   phoneNumber = opend_file_to_list[4].split(":")[1].strip()
   email = opend_file_to_list[5].split(":")[1].strip()
   my_age = int(opend_file_to_list[3].split(":")[1].strip())



   sim_provider_comapny = phoneNumber.strip()[:3]
   first_three_digits = int(id_number.strip()[:3])
   email_domain = email.split("@")[1].split(".")[0]


   print(sum([i for i in range(20,first_three_digits+1) if i % 8 == 0]))
   print(first_name)



   if my_age < 18:
      print("child")
   elif my_age <= 39:
     print("adult")
   elif my_age <= 59:
     print("Middle Age Adult")
   else:
     print("Senior Adult")


   if sim_provider_comapny == "059":
      print("JAWWAL")
   elif sim_provider_comapny == "056":
      print("OREDDO")
   else:
      print(f"your sim provider comapny code : {sim_provider_comapny} is not palestinian  ")



   print(f"your domain for your email is : {email_domain}")


   opend_file.close()

else:
   id_number = cs50.get_int("id number: ")
   first_name  = cs50.get_string("first name: ")
   YearOfBirth = cs50.get_int("Year Of Birth: ")
   myAge = CurrentYear - YearOfBirth
   mobile_number = cs50.get_string("mobile number: ")
   email_address = cs50.get_string("email address: ")

   data = open(file_source,"w")
   data.write(f"ID Number: {id_number}\n")
   data.write(f"First Name: {first_name}\n")
   data.write(f"Last Name: {last_name}\n")
   data.write(f"Age: {myAge}\n")
   data.write(f"Mobile Number: {mobile_number}\n")
   data.write(f"Email Address: {email_address}\n")
   data.close()
