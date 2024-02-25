def top_n(items, n):
    """
    Return the top n items in an array, in descending order.

    Args:
        items (array): list or array like object
        n (int) num of items to return
        
    Return:
        array: top n items in descending order
        
    Egs:
        >>> top_n([8, 3, 2, 7, 4], 3)
    """
    for i in range(n):  #keep sorting till we get the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]: #if this mitem is bigger than the next...
                items[j], items[j+1] = items[j+1], items[j] #swap them
            
    #get the last two items
    top_n = items[-n:]

    #return in descending order
    return top_n[::-1]