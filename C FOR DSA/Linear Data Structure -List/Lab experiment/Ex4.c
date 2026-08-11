#include <stdio.h>

int main()
{
    int book[50];
    int n = 0, choice, id, i, pos;

    while (1)
    {
        printf("\nLibrary Book Management\n");
        printf("1. Insert Book ID\n");
        printf("2. Delete Book ID\n");
        printf("3. Search Book ID\n");
        printf("4. Display Books\n");
        printf("5. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                /* Insert Book ID */
                if (n < 50)
                {
                    printf("Enter Book ID: ");
                    scanf("%d", &book[n]);

                    n++;

                    printf("Book ID added\n");
                }
                else
                {
                    printf("Library list is full\n");
                }
                break;

            case 2:
                /* Delete Book ID */
                printf("Enter Book ID to delete: ");
                scanf("%d", &id);

                pos = -1;

                for (i = 0; i < n; i++)
                {
                    if (book[i] == id)
                    {
                        pos = i;
                        break;
                    }
                }

                if (pos != -1)
                {
                    for (i = pos; i < n - 1; i++)
                    {
                        book[i] = book[i + 1];
                    }

                    n--;

                    printf("Book ID deleted\n");
                }
                else
                {
                    printf("Book ID not found\n");
                }
                break;

            case 3:
                /* Search Book ID */
                printf("Enter Book ID to search: ");
                scanf("%d", &id);

                pos = -1;

                for (i = 0; i < n; i++)
                {
                    if (book[i] == id)
                    {
                        pos = i;
                        break;
                    }
                }

                if (pos != -1)
                {
                    printf("Book ID found\n");
                }
                else
                {
                    printf("Book ID not found\n");
                }
                break;

            case 4:
                /* Display Books */
                if (n == 0)
                {
                    printf("No books available\n");
                }
                else
                {
                    printf("Available Book IDs: ");

                    for (i = 0; i < n; i++)
                    {
                        printf("%d ", book[i]);
                    }

                    printf("\n");
                }
                break;

            case 5:
                /* Exit */
                return 0;

            default:
                printf("Invalid choice\n");
        }
    }

    return 0;
}
