#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks the list if its a cycle
 *
 * @list: input pointer
 *
 * Return: 1 if is a cycle, else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}

