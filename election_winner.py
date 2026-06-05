"""
## 6. Election Winner from a Vote List  *(Easy)*

=================================================
ELECTION WINNER
=================================================

Problem Statement:
You are given a LIST of votes. Each element
of the list is the name (a single character or
a string) of the candidate that received that
vote.

Write a Python program that finds the WINNER
(the candidate with the highest number of
votes) and prints:
   - the winner's name
   - the total votes the winner received

If TWO or more candidates have the same highest
count, print all of them as a sorted list of
winners (a TIE).

-------------------------------------------------
Input Example 1:
['a', 'b', 'a', 'c', 'a']

Output Example 1:
Votes: {'a': 3, 'b': 1, 'c': 1}
Winner: a (3 votes)

-------------------------------------------------
Input Example 2:
['a', 'b', 'a', 'b', 'c']

Output Example 2:
Votes: {'a': 2, 'b': 2, 'c': 1}
Tie between: ['a', 'b'] (2 votes each)

-------------------------------------------------
Explanation:
For ['a', 'b', 'a', 'c', 'a']:
   a -> 3 votes  (highest)
   b -> 1 vote
   c -> 1 vote
Winner is 'a' with 3 votes.

For the second example two candidates share
the top count of 2, so the result is a TIE
between 'a' and 'b'.
=================================================

"""
# Election Winner Program

votes = input("Enter votes separated by spaces: ").split()

vote_count = {}

for vote in votes:
    if vote in vote_count:
        vote_count[vote] += 1
    else:
        vote_count[vote] = 1

print("Votes:", vote_count)

max_votes = max(vote_count.values())

winners = []

for candidate, count in vote_count.items():
    if count == max_votes:
        winners.append(candidate)

if len(winners) == 1:
    print(f"Winner: {winners[0]} ({max_votes} votes)")
else:
    winners.sort()
    print(f"Tie between: {winners} ({max_votes} votes each)")
