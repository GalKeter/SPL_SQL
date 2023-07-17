from persistence import *
def printTable(tableName, orderKey):
    print(tableName)
    dao = tableName.lower()
    for record in repo.__dict__[dao].find_all(orderKey): 
        print(record.to_str())

def printEmployeesReport():
    stmt = "SELECT employees.id, employees.name, employees.salary, branches.location FROM employees JOIN \
         branches ON employees.branche = branches.id ORDER BY employees.name ASC"
    for row in repo.execute_command(stmt):
        total_sales_income=0
        id = row[0]
        name = row[1]
        salary = row[2]
        location = row[3]
        for activ in repo.activities.find(activator_id=id):
            qauntity = activ.quantity
            product_id = activ.product_id
            price = repo.products.find(id=product_id)[0].price
            total_sales_income += qauntity*price
        print(name.decode() + " " + str(salary) + " " + location.decode() + " " + str(total_sales_income*(-1)))

def printActivitiesReport():
    stmt = "SELECT activities.date, products.description, activities.quantity, employees.name, suppliers.name FROM activities \
         JOIN products ON activities.product_id = products.id LEFT JOIN employees ON activities.activator_id = employees.id \
             LEFT JOIN suppliers ON activities.activator_id = suppliers.id ORDER BY activities.date ASC" 
    for row in repo.execute_command(stmt):
        toPrint = [b.decode() if type(b)==bytes else b for b in row]
        print(tuple(toPrint))


def main():
    #TODO: implement
    printTable("Activities", "date")
    printTable("Branches", "id")
    printTable("Employees", "id")
    printTable("Products", "id")
    printTable("Suppliers", "id")
    print()
    print("Employees report")
    printEmployeesReport()
    print()
    print("Activities report")
    printActivitiesReport()
        
if __name__ == '__main__':
    main()