#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 0 If there is no cycle.
 *         1 If there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *temp;

	if (list == NULL || list->next == NULL)
		return (0);

	current = list->next;
	temp = list->next->next;

	while (current && temp && temp->next)
	{
		if (current == temp)
			return (1);

		current = current->next;
		temp = temp->next->next;
	}

	return (0);
}
