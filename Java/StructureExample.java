//1.Documentation
//Example of structure of java program
//2.Package
//3.import
import java.util.Scanner;
//4.class
class StructureExample
{
    //5.variables
    int a;
    int b;
    //6.Constructors
    StructureExample(int a, int b)
    {
        this.a=a;
        this.b=b;
    }
    //7.methods
    void display()
    {
        System.out.println("Value of the A is:"+a);
        System.out.println("Value of the B is:"+b);
    }
    //8.Main method
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the value of A:");
        int a=sc.nextInt();
        System.out.println("Enter the value of B:");
        int b=sc.nextInt();
        StructureExample obj=new StructureExample(a,b);
        obj.display();
        sc.close();
    }

}
