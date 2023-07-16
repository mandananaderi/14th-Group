
print('Paragraph', '****************************************************')

myString = """previous research in this area provides fundamental contribution, 
still more research is needed to explore other facets of the branding theme. 
Loving fashion brands is an important aspect of research that is interesting and worth studying. 
Consumers love their fashion brands that are wellsuited to them and make them feel and look good. 
As a result, consumers develop a relationship with a brand feel emotionally associated to their brands. 
Consumer brand relationship in the last decade has gained much attention from both practitioners and academics. 
Understanding the relationships between consumers and their fashion brands has practical relevance 
to marketers due to the significant impact of this relationship on a companys profitability. 
Therefore, it is important to not only understand how relationships are formed between 
consumers and fashion brands, but we also must were aware of the factors that drive those relationships. """

toBe = ('am', 'is', 'are', 'was', 'were')

list1 = []
set1 = set()
for i in myString.split(' '):
    list1.append(i)
    if i in toBe:
        set1.add(i)

numberOfToBe = {i: myString.split(' ').count(i) for i in set1}

print('number of words: ', len(list1))
print('number of unique words: ', len(set((list1))))
print(set1)
print('numberOfToBe: ', numberOfToBe)