#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * free_lisadr - frees a lisadr list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_lisadr(lisadr *head)
{
	lisadr *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

/**
 * add_nodeadr - adds a new node at the beginning of a lisadr list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
lisadr *add_nodeadr(lisadr **head, listint_t *n)
{
	lisadr *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->adr = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * check_cycle - checks if a cycle is present in a linked list
 * @list: a pointer to a linked list
 *
 * Return: 0 if there are no loops present and 1 if present
*/
int check_cycle(listint_t *list)
{
	const listint_t *current;
	lisadr *addresses;
	lisadr *head;

	head = NULL;
	current = list;

	add_nodeadr(&head, list);
	while (current != NULL)
	{
		addresses = head;
		while (addresses != NULL)
		{
			if (addresses->adr == current->next)
			{
				free_lisadr(head);
				return (1);
			}
			add_nodeadr(&head, current->next);
			addresses = addresses->next;
		}
		current = current->next;
	}
	free_lisadr(head);
	return (0);
}
