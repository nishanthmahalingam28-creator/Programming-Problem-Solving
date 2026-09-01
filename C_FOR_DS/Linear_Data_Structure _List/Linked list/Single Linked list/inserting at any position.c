#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;

};

void InsertAtAnyposition(int value,struct node **head,int position)
{
    struct node *newnode=malloc(sizeof(struct node));
    newnode->data=value;
    newnode->next=NULL;

    if(position==1)
    {
        newnode->next=*head;
        *head=newnode;
    }

    struct node *temp=*head;
    for(int i=1;i<position-1 &&temp->next!=NULL;i++)
    {
        temp=temp->next;

    }
    

    if(temp->next==NULL)
    {
       free(newnode);
    }
    newnode->next=temp->next;
    temp->next=newnode;
}
    
void traverse(struct node *head)
{

}
