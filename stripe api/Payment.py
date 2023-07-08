def payment (liste):
    dct = liste["data"][0]["charges"]["data"][0]["metadata"] 
    yazdiricipay = dct["Customer Email"] + ","
    for number in range(1,16):
        try:
            yazdiricipay += dct[f"Order Item #{number}"]
        except:
            pass
    return yazdiricipay