#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @pointer_head: A pointer the head of the linked list.
 * @anums: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **pointer_head, int anums)
{
	listint_t *anode = *pointer_head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = anums;

	if (anode == NULL || anode->n >= anums)
	{
		new->next = anode;
		*pointer_head = new;
		return (new);
	}

	while (anode && anode->next && anode->next->n < anums)
		anode = anode->next;

	new->next = anode->next;
	anode->next = new;

	return (new);
}
