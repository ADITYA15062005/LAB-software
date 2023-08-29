import pandas as pd

data = {
    "Employee ID": ["161E90", "161F91", "161F99", "171E20", "171G30"],
    "Name": ["Raman", "Himadri", "Jaya", "Tejas", "Ajay"],
    "Age": [41, 38, 51, 30, 45],
    "Salary (PM)": [56000, 67500, 82100, 55000, 44000]
}

employee_df = pd.DataFrame(data)

def search_employee_data(parameter, value):
    if parameter == 1:  
        result = employee_df[employee_df["Age"] == value]
    elif parameter == 2:  
        result = employee_df[employee_df["Name"] == value]
    elif parameter == 3:  
        result = employee_df[employee_df["Salary (PM)"] == value]
    elif parameter == 4: 
        result = employee_df[employee_df["Salary (PM)"] >= value]
    elif parameter == 5:  
        result = employee_df[employee_df["Salary (PM)"] <= value]
    else:
        result = None
    return result

def main():
    print("Search Parameters:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (Exact)")
    print("4. Salary (>=)")
    print("5. Salary (<=)")
    choice = int(input("Enter the search parameter (1-5): "))
    value = None

    if choice in [1, 3, 4, 5]:
        value = float(input("Enter the value: "))
    elif choice == 2:
        value = input("Enter the name: ")

    result = search_employee_data(choice, value)

    if result is not None and not result.empty:
        print("Search Results:")
        print(result)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
