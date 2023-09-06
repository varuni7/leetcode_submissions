class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        #input : a list of strings 
        #output: int denotes no of mail address which receive mail 
        unique_addresses=set()
        for email_address in emails:
            
            #check for uppercase letters in email id 
            if email_address != email_address.lower():
                continue 
            local_name,domain_name=email_address.split("@")
            
            local_name=local_name.replace('.',"")
            local_name=local_name.split("+")[0]
            final_email_address=local_name + "@" +domain_name
            print(final_email_address)
            unique_addresses.add(final_email_address)
 
            
        return len(unique_addresses)
                
            
                
            
        
        