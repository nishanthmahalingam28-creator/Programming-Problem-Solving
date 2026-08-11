#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node *next;
};
void InsertAtEnd(int value, struct node **head)
{
	struct node *newnode=malloc(sizeof(struct node));
	newnode->data=value;
	newnode->next=NULL;
	
	if(*head==NULL)
	{
		*head=newnode;
		return;
	}
	
	struct node *temp=*head;
	while(temp->next !=NULL)
	{
		temp=temp->next;
	}
	temp->next=newnode;
}
void traverse(struct node *head)
{
	struct node *temp=head;
	while(temp!=NULL)
	{
		printf("%d",temp->data);
		temp=temp->next;
	}
	
	
}
int main()
{
	struct node *head=NULL;
	struct node *first=malloc(sizeof(struct node));
	first->data=10;
	first->next=NULL;
	struct node *second=malloc(sizeof(struct node));
	second->data=20;
	second->next=NULL;
	struct node *third=malloc(sizeof(struct node));
	third->data=30;
	third->next=NULL;
	
	head=first;
	first->next=second;
	second->next=third;
	
	
	printf("Before inserting");
	traverse(head);
	//Inserting at end
	InsertAtEnd(40,&head);
	printf("After inserting");
	traverse(head);
}
