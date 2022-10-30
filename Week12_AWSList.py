#AWS Service Inventory
#Create a list of services using Python. IE: S3, Lambda, EC2, etc

#The list should be empty initially.
service_list = []

#Populate the list using append or insert.
service_list.append('EC2')
service_list.append('S3')
service_list.append('IAM')
service_list.append('Lambda')
service_list.append('Eventbridge')
service_list.append('Cloud9')

#Print the list and the length of the list.
print(service_list)
print(len(service_list))

#Remove two specific services from the list by name or by index.
del service_list[1]
del service_list[4]

#Print the new list and the new length of the list.
print(service_list)
print(len(service_list))