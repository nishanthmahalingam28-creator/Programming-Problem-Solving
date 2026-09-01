#include <stdio.h>

int attendance[100];
int n = 0;

/* Add Student */
void addStudent()
{
    int roll;

    printf("Enter roll number: ");
    scanf("%d", &roll);

    attendance[n] = roll;
    n++;

    printf("Student added successfully\n");
}

/* Remove Student */
void removeStudent()
{
    int roll, i,j, found = 0;

    printf("Enter roll number to remove: ");
    scanf("%d", &roll);

    for (i = 0; i < n; i++)
    {
        if (attendance[i] == roll)
        {
            found = 1;

            for (j = i; j < n - 1; j++)
            {
                attendance[j] = attendance[j + 1];
            }

            n--;

            printf("Student removed successfully\n");
            break;
        }
    }

    if (found == 0)
    {
        printf("Student not found\n");
    }
}

/* Search Student */
void searchStudent()
{
    int roll, i, found = 0;

    printf("Enter roll no. to search: ");
    scanf("%d", &roll);

    for (i = 0; i < n; i++)
    {
        if (attendance[i] == roll)
        {
            found = 1;
            break;
        }
    }

    if (found)
    {
        printf("Student is present\n");
    }
    else
    {
        printf("Student is absent\n");
    }
}

/* Display Students */
void displayStudents()
{
    int i;

    if (n == 0)
    {
        printf("No students present\n");
        return;
    }

    printf("Student roll numbers:\n");

    for (i = 0; i < n; i++)
    {
        printf("%d ", attendance[i]);
    }

    printf("\n");
}

/* Main Function */
int main()
{
    int choice;

    while (1)
    {
        printf("\nStudent Attendance Management System\n");
        printf("1. Add student\n");
        printf("2. Remove student\n");
        printf("3. Search student\n");
        printf("4. Display students\n");
        printf("5. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                addStudent();
                break;

            case 2:
                removeStudent();
                break;

            case 3:
                searchStudent();
                break;

            case 4:
                displayStudents();
                break;

            case 5:
                printf("Program exited successfully\n");
                return 0;

            default:
                printf("Invalid choice\n");
        }
    }

    return 0;
}
