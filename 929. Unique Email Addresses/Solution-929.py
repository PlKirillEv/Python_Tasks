class Solution(object):
    def numUniqueEmails(self, emails):
        unique = set()

        for email in emails:
            local_part, domain = email.split("@")
            if "+" in local_part:
                local_part = local_part.split("+")[0]
            local_part = local_part.replace(".", "")
            unique.add(local_part + "@" + domain)

        return len(unique)
        