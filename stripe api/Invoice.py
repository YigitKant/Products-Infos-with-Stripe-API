def invoice (liste):
    try:
        email=liste["data"][0]["customer_email"]
        yazdiriciinvo=email+","
        description=liste["data"][0]["lines"]["data"][0]["description"]
        yazdiriciinvo+=description
    except KeyError as error:
        print(f"İnvoice çekerken hata aldım: KeyError{error}")
    except Exception as error2:
        print(f"İnvoice çekerken hata aldım: {error2}")
    finally:
        return yazdiriciinvo