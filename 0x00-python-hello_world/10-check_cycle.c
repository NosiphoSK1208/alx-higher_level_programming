#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @singly_list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *singly_list)
{
	listint_t *t_trle, *head;

	if (singly_list == NULL || singly_list->next == NULL)
		return (0);

	t_trle = singly_list->next;
	head = singly_list->next->next;

	while (t_trle && head && head->next)
	{
		if (t_trle == head)
			return (1);

		t_trle = t_trle->next;
		head = head->next->next;
	}

	return (0);
}
