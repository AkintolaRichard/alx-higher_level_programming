#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head pointer of the list
 * @number: integer which is the data in the node
 *
 * Return: address of the new node or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL, *current = NULL, *new = NULL;

	if (*head == NULL)
		return (NULL);
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (current != NULL)
	{
		if (current->n > new->n)
		{
			new->next = current;
			if (prev != NULL)
			{
				prev->next = new;
			}
			return (new);
		}
		prev = current;
		current = current->next;
	}
	return (NULL);
}
