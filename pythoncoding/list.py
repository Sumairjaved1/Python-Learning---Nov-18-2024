# import csv

# with open('test.csv', 'w', newline='') as fp:
#       fieldnames = ["Name", "Age", "School"]
#       a = csv.DictWriter(fp,fieldnames=fieldnames, delimiter= "\t")
#       a.writeheader()
#       a.writerows([{"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
#                   {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
#                   {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
#                   {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
#                   {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
#                   {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"}])

# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
# #       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})

# import csv

# with open('annual.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     counts = {}
#     for row in reader:
#         fav = row["Units"]
#         if fav in counts:
#             counts[fav] += 1
#         else:
#             counts[fav] = 1
# for fav in counts:
#     print(f"{fav}: {counts[fav]}")





      

