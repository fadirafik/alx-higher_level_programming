#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * struct listaddress - singly linked list
 * @adr: addreess of the other list
 * @next: points to the next node
 *
 * Description: singly linked list to keep track of the
 * addresses of the first list
*/
typedef struct listaddress
{
	listint_t *adr;
	struct listaddress *next;
} lisadr;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);
void free_lisadr(lisadr *head);
lisadr *add_nodeadr(lisadr **head, listint_t *n);

#endif /* LISTS_H */
