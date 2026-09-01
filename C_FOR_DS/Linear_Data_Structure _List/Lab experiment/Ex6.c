#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 50

struct Node {
    char song[MAX_LEN];
    struct Node *next;
};

struct Node *head = NULL;

/* Function prototypes */
void addSong(void);
void removeSong(void);
void moveUp(void);
void moveDown(void);
void display(void);
void freePlaylist(void);

/* Add a song to the end of the playlist */
void addSong(void)
{
    struct Node *newNode;
    struct Node *temp;

    newNode = (struct Node *)malloc(sizeof(struct Node));

    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }

    printf("Enter song name: ");
    scanf(" %49[^\n]", newNode->song);

    newNode->next = NULL;

    if (head == NULL) {
        head = newNode;
    } else {
        temp = head;

        while (temp->next != NULL) {
            temp = temp->next;
        }

        temp->next = newNode;
    }

    printf("Song added successfully.\n");
}

/* Remove a song from the playlist */
void removeSong(void)
{
    char name[MAX_LEN];
    struct Node *temp = head;
    struct Node *prev = NULL;

    printf("Enter song name to remove: ");
    scanf(" %49[^\n]", name);

    while (temp != NULL && strcmp(temp->song, name) != 0) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Song not found.\n");
        return;
    }

    if (prev == NULL) {
        head = temp->next;
    } else {
        prev->next = temp->next;
    }

    free(temp);

    printf("Song removed successfully.\n");
}

/* Move a song one position upward */
void moveUp(void)
{
    char name[MAX_LEN];
    struct Node *prev = NULL;
    struct Node *curr = head;

    printf("Enter song name to move up: ");
    scanf(" %49[^\n]", name);

    if (head == NULL || head->next == NULL) {
        printf("Cannot move.\n");
        return;
    }

    if (strcmp(head->song, name) == 0) {
        printf("Song is already at the top.\n");
        return;
    }

    while (curr != NULL && curr->next != NULL) {

        if (strcmp(curr->next->song, name) == 0) {
            char temp[MAX_LEN];

            strcpy(temp, curr->song);
            strcpy(curr->song, curr->next->song);
            strcpy(curr->next->song, temp);

            printf("Song moved up.\n");
            return;
        }

        prev = curr;
        curr = curr->next;
    }

    printf("Song not found.\n");
}

/* Move a song one position downward */
void moveDown(void)
{
    char name[MAX_LEN];
    struct Node *curr = head;

    printf("Enter song name to move down: ");
    scanf(" %49[^\n]", name);

    if (head == NULL || head->next == NULL) {
        printf("Cannot move.\n");
        return;
    }

    while (curr != NULL && curr->next != NULL) {

        if (strcmp(curr->song, name) == 0) {

            char temp[MAX_LEN];

            strcpy(temp, curr->song);
            strcpy(curr->song, curr->next->song);
            strcpy(curr->next->song, temp);

            printf("Song moved down.\n");
            return;
        }

        curr = curr->next;
    }

    /* Check if the requested song is the last song */
    if (curr != NULL && strcmp(curr->song, name) == 0) {
        printf("Song is already at the bottom.\n");
        return;
    }

    printf("Song not found.\n");
}

/* Display all songs */
void display(void)
{
    struct Node *temp = head;

    if (head == NULL) {
        printf("Playlist is empty.\n");
        return;
    }

    printf("\nPlaylist:\n");

    while (temp != NULL) {
        printf("%s\n", temp->song);
        temp = temp->next;
    }

    printf("\n");
}

/* Free all allocated memory */
void freePlaylist(void)
{
    struct Node *temp;

    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

/* Main function */
int main(void)
{
    int choice;

    while (1) {

        printf("\n===== MUSIC PLAYLIST MENU =====\n");
        printf("1. Add Song\n");
        printf("2. Remove Song\n");
        printf("3. Move Song Up\n");
        printf("4. Move Song Down\n");
        printf("5. Display Playlist\n");
        printf("6. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {

            case 1:
                addSong();
                break;

            case 2:
                removeSong();
                break;

            case 3:
                moveUp();
                break;

            case 4:
                moveDown();
                break;

            case 5:
                display();
                break;

            case 6:
                freePlaylist();
                printf("Exiting program...\n");
                return 0;

            default:
                printf("Invalid choice.\n");
        }
    }

    return 0;
}
