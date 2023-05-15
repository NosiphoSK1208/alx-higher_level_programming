#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @ahead: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **ahead)
{
  listint_t *prvs = NULL;
  listint_t *crrnt = *ahead;
  listint_t *next = NULL;

  while (crrnt)
    {
      next = crrnt->next;
      crrnt->next = prvs;
      prvs = crrnt;
      crrnt = next;
    }

  *ahead = prvs;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @ahead: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **ahead)
{
  listint_t *aslw = *ahead, *fast = *ahead, *tmpo = *ahead, *dp = NULL;

  if (*ahead == NULL || (*ahead)->next == NULL)
    return (1);

  while (1)
    {
      fast = fast->next->next;
      if (!fast)
	{
	  dp = aslw->next;
	  break;
	}
      if (!fast->next)
	{
	  dp = aslw->next->next;
	  break;
	}
      aslw = aslw->next;
    }

  reverse_listint(&dp);

  while (dp && tmpo)
    {
      if (tmpo->n == dp->n)
	{
	  dp = dp->next;
	  tmpo = tmpo->next;
	}
      else
	return (0);
    }

  if (!dp)
    return (1);

  return (0);
}
