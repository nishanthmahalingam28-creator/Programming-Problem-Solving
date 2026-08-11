//creating node
#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data; //data
	struct node *next; // pointer
};
int main()
{
	struct node *head=malloc(sizeof(struct node));
	head->data=45;
	head->next=NULL;
	return 0;
}
