class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            local,domain  = email.split("@")
            
            local = local.split("+")[0]
            local = "".join(local.split("."))
            email_set.add(local + "@" +domain)
            
        return len(email_set)