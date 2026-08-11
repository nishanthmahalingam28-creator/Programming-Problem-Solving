#include<stdio.h>
#define SIZE 100
int arr[SIZE];
int n;
int main()
{
	printf("Enter the number of elements(n):");
	scanf("%d",&n);
	if(n<=SIZE)
	{
		printf("Enter %d elements:\n",n);
		for(int i=0;i<n;i++){
			scanf("%d",&arr[i]);
		}
	}
	else
	{
		printf("Requested to enter the size below the maximum size");
	}
	for(int j = 0; j < n ; j++)
	{
		printf("%d",arr[j]);
	}
	
	return 0;
}
