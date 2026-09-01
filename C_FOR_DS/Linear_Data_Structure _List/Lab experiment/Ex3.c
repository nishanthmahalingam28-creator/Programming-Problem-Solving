#include <stdio.h>

int main()
{
    long contact[50];
    int n = 0, choice, i, pos;
    long num;

    while (1)
    {
        printf("\nMobile Contact List\n");
        printf("1. Add contact\n");
        printf("2. Delete contact\n");
        printf("3. Search contact\n");
        printf("4. Display contact\n");
        printf("5. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                if (n < 50)
                {
                    printf("Enter contact number: ");
                    scanf("%ld", &contact[n]);

                    n++;

                    printf("Contact added successfully\n");
                }
                else
                {
                    printf("Contact list is full\n");
                }
                break;

            case 2:
                printf("Enter contact number to delete: ");
                scanf("%ld", &num);

                pos = -1;

                for (i = 0; i < n; i++)
                {
                    if (contact[i] == num)
                    {
                        pos = i;
                        break;
                    }
                }

                if (pos != -1)
                {
                    for (i = pos; i < n - 1; i++)
                    {
                        contact[i] = contact[i + 1];
                    }

                    n--;

                    printf("Contact deleted\n");
                }
                else
                {
                    printf("Contact not found\n");
                }
                break;

            case 3:
                printf("Enter contact number to search: ");
                scanf("%ld", &num);

                pos = -1;

                for (i = 0; i < n; i++)
                {
                    if (contact[i] == num)
                    {
                        pos = i;
                        break;
                    }
                }

                if (pos != -1)
                {
                    printf("Contact found\n");
                }
                else
                {
                    printf("Contact not found\n");
                }
                break;

            case 4:
                if (n == 0)
                {
                    printf("No contacts available\n");
                }
                else
                {
                    printf("Contact List:\n");

                    for (i = 0; i < n; i++)
                    {
                        printf("%ld\n", contact[i]);
                    }
                }
                break;

            case 5:
                return 0;

            default:
                printf("Invalid choice\n");
        }
    }

    return 0;
}
