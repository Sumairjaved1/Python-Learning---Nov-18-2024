import csv

with open('test.csv', 'w', newline='') as fp:
      fieldnames = ["Name", "Age", "School"]
      a = csv.DictWriter(fp,fieldnames=fieldnames, delimiter= "\t")
      a.writeheader()
      a.writerows([{"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
                  {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
                  {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
                  {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
                  {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"},
                  {"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"}])

#       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
#       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
#       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
#       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
#       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})
#       a.writerow({"Name" : "SumairJaved", "Age" : 35, "School" : "Sir Syed"})



      

