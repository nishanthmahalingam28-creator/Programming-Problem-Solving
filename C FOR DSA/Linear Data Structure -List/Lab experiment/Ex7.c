#include <stdio.h>
#include <string.h>

#define MAX 50

char back[MAX][50];
char forward[MAX][50];

int topB = -1;
int topF = -1;

char current[50] = "Home";

/* Visit a new page */
void visit(char page[])
{
    strcpy(back[++topB], current);
    strcpy(current, page);

    /* Clear forward history */
    topF = -1;
}

/* Go back to the previous page */
void backPage()
{
    if (topB == -1)
    {
        printf("No back page\n");
    }
    else
    {
        /* Save current page in forward stack */
        strcpy(forward[++topF], current);

        /* Move to previous page */
        strcpy(current, back[topB--]);
    }
}

/* Go forward to the next page */
void forwardPage()
{
    if (topF == -1)
    {
        printf("No forward page\n");
    }
    else
    {
        /* Save current page in back stack */
        strcpy(back[++topB], current);

        /* Move to next page */
        strcpy(current, forward[topF--]);
    }
}

int main()
{
    visit("Google");
    visit("YouTube");
    visit("Wikipedia");

    printf("Current: %s\n", current);

    backPage();
    printf("After Back: %s\n", current);

    backPage();
    printf("After Back: %s\n", current);

    forwardPage();
    printf("After Forward: %s\n", current);

    return 0;
}
