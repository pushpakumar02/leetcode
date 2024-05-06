class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local, domain))
        return len(unique)


# Intuition and Approach:

# - We're given a list of email addresses `emails`.
# - To count the number of unique email addresses, we can use a set to store unique combinations of local names and domains.
# - We iterate through each email address in the list:
#   - Split the email address into local name and domain using the "@" symbol.
#   - Process the local name:
#     - Remove everything after the "+" symbol (if present) by splitting the local name at "+" and taking the first part.
#     - Remove all "." characters from the local name.
#   - Add the processed local name and domain as a tuple to the set.
# - Finally, return the length of the set, which represents the number of unique email addresses.

# Time Complexity: O(n * m), where n is the number of email addresses and m is the maximum length of an email address. This is because we iterate through each email address once and perform string manipulations, which take linear time.

# Space Complexity: O(n * m), where n is the number of email addresses and m is the maximum length of an email address. The set can potentially store all unique email addresses.
