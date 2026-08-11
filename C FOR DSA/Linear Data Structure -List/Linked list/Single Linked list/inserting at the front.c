#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node *next;
};
//Inserting value
void InsertATFront(int newdata,struct node **head)
{
	struct node *newNode=malloc(sizeof(struct node));
	newNode->data=newdata;
	newNode->next=*head;
	*head=newNode;
	
}
//transverse 
void transverse(struct node *head)
{
	struct node *temp=head;
	printf("Linked list:");
	while(temp!=NULL)
	{
		printf("%d",temp->data);
		temp=temp->next;
	}
	printf("\n");
}
//main function
int main()
{
	struct node *first=malloc(sizeof(struct node));
	first->data=10;
	struct node *second=malloc(sizeof(struct node));
	second->data=20;
	struct node*third=malloc(sizeof(struct node));
	third->data=30;
	first->next=second;
	second->next=third;
	third->next=NULL;
	struct node *head=first;
	printf("origin list\n");
	transverse(head);
	printf("Inserting value at the front");
	InsertATFront(5,&head);
	printf("After insertion");
	transverse(head);
	return 0;
	
}
