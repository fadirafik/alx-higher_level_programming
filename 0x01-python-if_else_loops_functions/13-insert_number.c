#include "lists.h"

/**
 * insert_node - inserts a new node in the already sorted
 * linked list
 * @head: a pointer to the lists head
 * @number: the number to be inserted in the linked list
 * Return: a pointer to the newly inserted node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *prev;
	listint_t *new;

	temp = *head;
	prev = temp;

	while (temp != NULL)
	{
		if (number < temp->n)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);

			new->n = number;
			new->next = temp;
			prev->next = new;
			return (new);
		}
		prev = temp;
		temp = temp->next;
	}
	return (NULL);
}
