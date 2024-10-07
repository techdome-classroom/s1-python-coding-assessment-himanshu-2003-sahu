def decode_message(s: str, p: str) -> bool:
    def match_helper(s_idx, p_idx):
       
        if s_idx == len(s) and p_idx == len(p):
            return True
        
        if p_idx == len(p):
            return False

       
        if p[p_idx] == "*":
          
            return match_helper(s_idx, p_idx + 1) or (
                s_idx < len(s) and match_helper(s_idx + 1, p_idx)
            )

       
        if s_idx < len(s) and (p[p_idx] == "?" or p[p_idx] == s[s_idx]):
            
            return match_helper(s_idx + 1, p_idx + 1)

      
        return False

    
    return match_helper(0, 0)



print(decode_message("aa", "a"))  
print(decode_message("aa", "*"))
print(decode_message("cb", "?a"))  
print(decode_message("abc", "a*c"))  
print(decode_message("abc", "a?c"))  
