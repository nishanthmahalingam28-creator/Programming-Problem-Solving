#include<stdio.h>
#define SIZE 100
int arr[SIZE];
int main()
{
	int n;
	int value;
	int index=-1;
	printf("Enter the number of element(n):\n");
	scanf("%d",&n);
	//check the number of element with in size of the array
	if(n>SIZE)
	{
		printf("The  number of element is greater than size of the array\n");
	}
	//Inserting element in array
	printf("Enter the element in array\n") ;
	for(int i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	//Read the value
	printf("Enter the value to be search:\n");
	scanf("%d",&value);
	//Searching the element
	for(int i=0;i<n;i++){
		if(value==arr[i])
		{
			 index=i;
			 break;
		}
	}
	//checking the element is found or not
	if(index == -1 )
	{
		printf("Element is not found\n");
	}
	else
	{
		printf("Element is found\n");
		printf("The position of the value is %d",index+1);
	}
}
