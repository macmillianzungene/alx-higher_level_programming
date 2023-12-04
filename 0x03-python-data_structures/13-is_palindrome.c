#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = *head, *next;
    int ispalin = 1;

    if (head == NULL || *head == NULL || (*head)->next == NULL)
        return (1);

    while (fast && fast->next)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    prev->next = NULL;
    prev = NULL;

    while (slow)
    {
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    fast = *head;
    slow = prev;

    while (slow && ispalin)
    {
        if (slow->n != fast->n)
            ispalin = 0;
        slow = slow->next;
        fast = fast->next;
    }

    return (ispalin);
}

