#include <stdio.h>

#define MAX_SEATS 30

int seat[MAX_SEATS];
int count = 0;

int main()
{
    int choice, num, i, found;

    while (1)
    {
        printf("\n===== BUS SEAT RESERVATION =====\n");
        printf("1. Book Seat\n");
        printf("2. Cancel Seat\n");
        printf("3. Search Seat\n");
        printf("4. Display Booked Seats\n");
        printf("5. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            /* Book Seat */
            case 1:
                if (count < MAX_SEATS)
                {
                    printf("Enter seat number: ");
                    scanf("%d", &num);

                    /* Check whether seat is already booked */
                    found = 0;

                    for (i = 0; i < count; i++)
                    {
                        if (seat[i] == num)
                        {
                            found = 1;
                            break;
                        }
                    }

                    if (found)
                    {
                        printf("Seat is already booked.\n");
                    }
                    else
                    {
                        seat[count] = num;
                        count++;

                        printf("Seat booked successfully.\n");
                    }
                }
                else
                {
                    printf("All seats are booked.\n");
                }
                break;

            /* Cancel Seat */
            case 2:
                printf("Enter seat number to cancel: ");
                scanf("%d", &num);
				int i,j;
                found = 0;

                for (i = 0; i < count; i++)
                {
                    if (seat[i] == num)
                    {
                        found = 1;

                        /* Shift remaining seats left */
                        for (j = i; j < count - 1; j++)
                        {
                            seat[j] = seat[j + 1];
                        }

                        count--;

                        printf("Seat cancelled successfully.\n");
                        break;
                    }
                }

                if (!found)
                {
                    printf("Seat not found.\n");
                }
                break;

            /* Search Seat */
            case 3:
                printf("Enter seat number to search: ");
                scanf("%d", &num);

                found = 0;

                for (i = 0; i < count; i++)
                {
                    if (seat[i] == num)
                    {
                        found = 1;
                        break;
                    }
                }

                if (found)
                {
                    printf("Seat %d is booked.\n", num);
                }
                else
                {
                    printf("Seat %d is available.\n", num);
                }
                break;

            /* Display Booked Seats */
            case 4:
                if (count == 0)
                {
                    printf("No seats are booked.\n");
                }
                else
                {
                    printf("Booked Seats:\n");

                    for (i = 0; i < count; i++)
                    {
                        printf("%d\n", seat[i]);
                    }
                }
                break;

            /* Exit */
            case 5:
                printf("Thank you!\n");
                return 0;

            /* Invalid Choice */
            default:
                printf("Invalid choice.\n");
        }
    }

    return 0;
}
