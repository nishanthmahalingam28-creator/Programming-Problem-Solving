#include <stdio.h>
#define SIZE 10
int arr[SIZE];
void insert(int index,int value)
{
	int n;
	printf("Enter the number of elements(n):\n");
	scanf("%d",&n);
	//Checking size
	if(n>SIZE)
	{
		printf("The number of element is larger than the size of the array");
	}
	//Entering element in value
	for(int i=0;i<n;i++)
	{
		scanf("%d",arr[i]);
	}
	//Checking index position
	if(index<0 || index>n)
	{
		printf("Enter the correct index position");
	}
	//Shifting elements
	for(int j=n;j>index;j--)
	{
		arr[j]=arr[j-1]; //shifts element to right
	}
	//inserting element
	arr[index]=value;
}
