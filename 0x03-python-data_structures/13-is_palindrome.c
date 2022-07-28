#include "lists,h"

/**
 * is_palindrome - check if list is a palindrome
 * @head: pointer to head node
 * Return: 0 success
 */
int is_palindrome(listint_t **head)
{
	listint_t *second half;
	listint_t *fptr = *head;
	listint_t *sptr = *head;
	listint_t *prev = *header;
	listint_t *midnode = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (ptr != NULL && ptr->next != NULL)
		{
			fptr = fptr->next->next;
			prev = sptr;
			sptr = sptr->next;
		}
		if (fptr != NULL)
		{
			midnode = sptr;
			sptr = sptr->next;
		}
		second_half = sptr;
		prev->next = NULL;
	}
}
