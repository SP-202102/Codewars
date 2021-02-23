def generate_bc(inputUrl):
    outputHtml = ""
# split input
    elementList = inputUrl.split( "/" )

# apply rules

#formate output elements

# construct output
    outputHtml = "/".join(elementList)
    print(elementList)
    print(outputHtml)
    return (outputHtml)
    
print(generate_bc( "test/test2"))