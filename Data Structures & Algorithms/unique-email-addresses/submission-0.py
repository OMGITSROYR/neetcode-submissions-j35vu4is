class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
       found = set() 

       for email in emails:
        local = email.split('@')[0]
        domain = email.split('@')[1]

        if "+" in local:
            local = local.split('+')[0]

        print(local)

        while "." in local:
            new = "".join(local.split('.'))
            local = new

        final_email = local + "@" + domain

        print(final_email)

        if final_email in found:
            continue
        else:
            found.add(final_email)

       return len(found)