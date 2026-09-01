class Variables
{
    //Instance Variables
    int a=10;
    int b=20;
    //static variable
    static String name="Java Programming";
    void display()
    {
        //Local Variables
        int c=30;
        int d=40;
        System.out.println("Instance Variable a: "+a);
        System.out.println("Instance Variable b: "+b);
        System.out.println("Static Variable name: "+name);
    }
   
    
    public static void main(String args[])
    {
        Variables v=new Variables();
        v.display();
    }
}