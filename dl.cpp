
#include<stdio.h>
#include<stdlib.h>
void createlist(int);
void display();
void insertatbeg();
void insertatend();
void insertatpos();
struct node{
struct node *prev;
int data;
struct node *next;
}node;
struct node *start,*temp,*temp1,*newnode;
int main()
{
int n;
start=(struct node*)malloc(sizeof(node));
if(start==NULL)
{
printf("memory overflow\n");
exit(0);
}
printf("enter the number of nodes you want to store\n");
scanf("%d",&n);
printf("enter the data for first node\n");
scanf("%d",&start->data);
start->next=NULL;
start->prev=NULL;
createlist(n);
display();
return(0);
insertatbeg();
insertatpos();
}
void createlist(int n)
{
int i;
temp=start;
for(i=1;i<n;i++)
{ 
newnode=(struct node*)malloc(sizeof(node));
if(newnode==NULL)
{
printf("memory overflow\n");
exit(0);
}
printf("enter data for node \n");
scanf("%d",&newnode->data);
newnode->next=NULL;
temp->next=newnode;
newnode->prev=temp;
temp=temp->next;
}
}
void display()
{
int i=1;
temp=start;
while(temp->next!=NULL)
{
++i;
printf("\ndata is = %d",temp->data);
temp=temp->next;
}
printf("\ndata is = %d",temp->data);
printf("\nthere are %d nodes in the doubly linked list",i);
}
void insertatbeg()
{
temp=start;
newnode=(struct node*)malloc(sizeof(node));
if(newnode==NULL)
{
printf("memory overflow\n");
exit(0);
}
printf("\n enter the data for newnode");
scanf("%d",&newnode->data);
newnode->prev==NULL;
temp->prev=newnode;
newnode->next=temp;
start=newnode;
display();
}
void insertatpos()
{
int num;
temp=start;
newnode=(struct node*)malloc(sizeof(node));
if(newnode==NULL)
{
printf("memory overflow\n");
exit(0);
}
printf("\nenter the data for newnode");
scanf("%d",&newnode->data);
printf("\nenter the data of node after which you want to insert newnode");
scanf("%d",&num);
while(temp->next!=NULL)
{
if(temp->data==num)
{
newnode->next=temp->next;
newnode->prev=temp;
temp->next=newnode;
newnode->next->prev=newnode;
}
temp=temp->next;
}
display();
}

