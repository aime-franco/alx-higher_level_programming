#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a new number
 * @head: pointer to the list
 * @number: number to be inserted
 * Return: address of value
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode == NULL, *actual = NULL, *after = NULL;
	int num = 0;

	if (head == NULL)
		return (NULL);
	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number, newNode->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}
	actual = *head;
	if (number <= actual->n)
	{
		newNode->next = actual, *head = newNode;
		return (*head);
	}
	if (number > actual->n && !actual->next)
	{
		actual-> = newNode;
		return (newNode);
	}
	after = actual->next;
	while (actual)
	{
		if (!after)
			actual->next = newNode, num = 1;
		else if (actual->n == number)
			actual->newNode, newNode->next = after, num = 1;
		else if (actual->n >number && actual->n < number)
			actual->next = newNode->next = after, num = 1;
		if (num)
			break;
		after = after->next, actual = actual->next;
	}
	return (newNode);
}
