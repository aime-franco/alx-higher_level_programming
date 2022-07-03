#include "lists.h"

/**
 * check_cycle - checks the cycles in the singly linked listt
 * @list: pointer to the list
 * Return: 0 success
 */
int check_cycle(listint_t *list)
{
	listint_t *p2;
	listint_t *before;

	p2 = list;
	before = list;
	while (list && p2 && p2->next)
	{
		list = before;
		before = p2;
		if (list == p2)
		{
			while (1)
			{
				p2 = before;
				while (p2->next != list && p2->next != before)
				{
					p2 = p2->next;
				}
				if (p2->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
			
	}
	return (0);
}
