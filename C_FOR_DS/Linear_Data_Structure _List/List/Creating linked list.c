//creating the linked list
#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node *next;
};
int main()
{
	//first node
	struct node *first=malloc(sizeof(struct node));
	first->data=5;
	first->next=NULL;
	//second node
	struct node *second=malloc(sizeof(struct node));
	second->data=10;
	second->next=NULL;
	//third node
	struct node *third=malloc(sizeof(struct node));
	third->data=20;
	third->next=NULL;
	first->next=second;
	second->next=third;
	
	
	//printing linked list
	printf("Linked list");
	struct node *temp=first;
	while(temp!=NULL)
	{
		printf("%d",temp->data);
		temp=temp->next;
	}
}
