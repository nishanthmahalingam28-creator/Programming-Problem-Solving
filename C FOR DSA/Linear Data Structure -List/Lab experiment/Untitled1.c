#include <stdio.h>

#define MAX 100

struct Student
{
    int roll;
    char name[50];
    float marks;
};

int main()
{
    struct Student students[MAX];
    int n, i;

    printf("Enter the number of students: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        printf("\nEnter details of student %d\n", i + 1);

        printf("Roll number: ");
        scanf("%d", &students[i].roll);

        printf("Name: ");
        scanf("%s", students[i].name);

        printf("Marks: ");
        scanf("%f", &students[i].marks);
    }

    printf("\nStudent Records\n");
    printf("-------------------------\n");

    for (i = 0; i < n; i++)
    {
        printf("Roll number: %d\n", students[i].roll);
        printf("Name: %s\n", students[i].name);
        printf("Marks: %.2f\n", students[i].marks);
        printf("-------------------------\n");
    }

    return 0;
}
