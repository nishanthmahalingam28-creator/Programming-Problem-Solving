//1.Documentation
//Structure of Java Program
//2.Package
package packageName;
//3.Import 
import java.util.*;
//4.class
class StructureOfJava
{
    //5.variables
    int x;
    //6.Constructors
    StructureOfJava()
    {
        x=10;
    }
    //7.methods
    void display()
    {
        System.out.println("Value of the X is:"+x);

    }
    //8.Main method
    public static void main(String args[])
    {
        StructureOfJava obj=new StructureOfJava();
        obj.display();
    }

}