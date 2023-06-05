def FA(s):
    size = 0
    # Scan complete string and make sure that it contains only 'a' & 'b'
    for i in s:
        if i == 'a' or i == 'b':
            size += 1
        else:
            return "Rejected"

    # After checking that it contains only 'a' & 'b', check its length (should be at least 3)
    if size >= 3:
        # Check the last 3 elements
        if s[size - 3] == 'b':
            if s[size - 2] == 'b':
                if s[size - 1] == 'a':
                    return "Accepted"  # If all 3 conditions are true
                else:
                    return "Rejected"  # If 3rd condition is false
            else:
                return "Rejected"  # If 2nd condition is false
        else:
            return "Rejected"  # If 1st condition is false
    else:
        return "Rejected"  # If length is less than 3

inputs = ['bba', 'ababbba', 'abba', 'abb', 'baba', 'bbb', '']
for i in inputs:
    print(FA(i))
