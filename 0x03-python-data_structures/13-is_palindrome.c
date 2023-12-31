#include "lists.h"
/**
 * is_palindrome - checks if a linked list has a palindrome
 * in it
 * @head: a pointer to a head of a linked list
 * Return: 0 if not a palindrome and 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *paral;
	listint_t *temp;
	listint_t *end;

	end = *head;
	paral = NULL;

	if (!*head)
	{
		return (1);
	}
	while (end)
	{
		temp = malloc(sizeof(listint_t));
		if (!temp)
			return (0);
		temp->n = end->n;
		temp->next = paral;
		paral = temp;
		end = end->next;
	}
	while (paral && *head)
	{
		if (paral->n != (*head)->n)
		{
			return (0);
		}
		paral = paral->next;
		*head = (*head)->next;
	}
	free_listint(temp);
	return (1);
}
