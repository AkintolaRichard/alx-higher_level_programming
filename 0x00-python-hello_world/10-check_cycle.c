#include "lists.h"

/**
 * check_cycle - checks id a singly linked list has a cycle in it.
 * @list: head of a singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_runner, *fast_runner;

	if (list == NULL || list->next == NULL)
		return (0);
	slow_runner = list->next;
	fast_runner = list->next->next;

	while (slow_runner && fast_runner && fast_runner->next)
	{
		if (fast_runner == slow_runner)
			return (1);
		slow_runner = slow_runner->next;
		fast_runner = fast_runner->next->next;
	}
	return (0);
}
