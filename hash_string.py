def hash_string(keyword,buckets):
    
    L=[[".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
       [46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]]
       
    count=0
    for i in keyword:
        j=0
        while j<len(L[0]):
            if i==L[0][j]:
                count=count+L[1][j]
                break
            else:
                j=j+1
                
    return count%buckets
    
print hash_string("a",12)
print hash_string("b",12)
print hash_string("a",13)
print hash_string("au",12)
print hash_string('udacity',12)
print hash_string('udacity',14)
print hash_string('Udacity',14)
print hash_string('CS101',20)
print hash_string('searchwithpeter.info',73)
print hash_string('',12)
