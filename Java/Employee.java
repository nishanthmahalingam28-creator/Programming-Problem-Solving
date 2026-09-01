/*Develop a Java application to demonstrate the concepts of class and object by 
storing and displaying employee details. Explain how objects are created during 
program execution.*/

import java.util.Scanner;
class Employee
{
    int id;
    String name;
    double salary;
    //Constuctor
    Employee(int id,String name,double salary)
    {
        this.id=id;
        this.name=name;
        this.salary=salary;
    }
    //Method to display employee details
    void display()
    {
        System.out.println("Employee ID: "+id);
        System.out.println("Employee Name: "+name);
        System.out.println("Employee Salary: "+salary);
    }
    //main method
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Employee ID:");
        int id=sc.nextInt();
        System.out.println("Enter Employee Name:");
        String name=sc.next(); 
        System.out.println("Enter Employee Salary:");
        double salary=sc.nextDouble();
        Employee emp1=new Employee(id,name,salary);
        emp1.display();
        sc.close();
    }
}