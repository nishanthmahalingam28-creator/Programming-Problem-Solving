class Details
{
    //private
    private int pin=1234;
    //Default
    int age=25;
    //protected
    protected String name="john";
    //public
    public String city="New York";
    public void display()
    {
        System.out.println("Private Pin: "+pin);
        System.out.println("Default Age: "+age);
        System.out.println("Protected Name: "+name);
        System.out.println("Public City: "+city);
    }
}
class Accessmodifiers
{
    public static void main(String args[])
    {
       
        Details d=new Details();
        d.display();
    }
}