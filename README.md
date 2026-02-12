QUICKSORT ALGORITHM
Quicksort is a classic example of the Divide and Conquer strategy. It focuses
on the idea that it is much easier to sort two small lists than one large one.
Quicksort divides the list based on the values of the elements themselves.
1. Choosing the Pivot
First, we select an element from the array to be the "pivot." The pivot acts as a
benchmark. Every other number in the array will be compared against this
value. You can pick the first element, the last element, or even a random one.
2. The Partitioning Process
This is the "workhorse" algorithm. We rearrange the array so that:
• Every element smaller than the pivot is moved to its left.
• Every element larger than the pivot is moved to its right.
• The pivot itself ends up in its exact sorted position, where it will stay
forever.
3. Recursive Division
Now that the pivot has split the array into two "sub-arrays" (the smaller-than-
pivot side and the larger-than-pivot side), we treat those two sides as brand-
new problems. We pick a new pivot for the left side and a new pivot for the
right side, then partition them again.
4. The Base Case
We continue this division until we reach a sub-array that has only one element
(or zero). At this point, the logic stops because a single number is already
"sorted" by default. As the recursion "unwinds," the entire array is revealed to
be in perfect order.
Complexity and PerformanceThe efficiency of Quicksort depends on how "balanced" the partitions are.
• Average and Best Case: If the pivot usually lands somewhere in the
middle of the sorted range, the algorithm performs at $O (n \log n) $.
This is very fast and is the reason Quicksort is used in many built-in
programming libraries.
• Worst Case: If the pivot is always the smallest or largest element (like
trying to sort an already sorted list by picking the first element as the
pivot), the algorithm slows down to $O(n^2) $.
• Space: The algorithm is efficient with memory because it primarily uses
the "call stack" for recursion, typically requiring $O (\log n) $ space.
