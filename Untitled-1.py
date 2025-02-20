def find_keyword(keywords, document):
    result = []
    
    for keyword in keywords:
        start = 0
        
        while True:
            start = document.find(keyword, start)
            if start == -1:
                break
            
            result.append(keyword)
            start += 1
            
    return result

doc1 = "ABCD"
doc2 = "ABCDABCD"

print(find_keyword(["AB", "AC", "BC", "ABD"], doc1))

print(find_keyword(["AB", "AC", "BC", "ABD"], doc2))

