import pandas as pd
print(pd.Series([1, 2, 3, 4, 5]))
data = {
    "Name" :["Shubham","Sunil","Vivek"],
    "City" :["Lucknow","Deoria","Basti"],
    "Marks":[90,45,78]
}
dt = pd.DataFrame(data)
print(dt)
print(dt.info())
print(dt.describe())
dt.to_csv("Data.csv",index=False)
dt_read = pd.read_csv("Data.csv")
print(dt_read)