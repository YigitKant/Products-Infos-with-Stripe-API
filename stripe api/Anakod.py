import stripe
import time
from datetime import datetime
from Payment import payment
from Invoice import invoice
from idci import id_checker_invoice, id_checker_payment
from discord_webhook import DiscordWebhook, DiscordEmbed

while True:
    try:
        print("a")
        zaman=datetime.now()
        zaman=str(zaman)

        file1=open("steamid.txt","r",encoding="utf8")
        data=file1.read()
        file1.close()

        stripe.max_network_retries=999
        stripe.api_key = "sk_test_26PHem9AhJZvU623DfE1x4sd" #stripe api key (this is test api) you must change that

        odeme=stripe.PaymentIntent.list(limit=1)
        fatura=stripe.Invoice.list(limit=1)
        
        status=odeme["data"][0]["status"]
        description=odeme["data"][0]["description"]
        amount_received = odeme["data"][0]["amount_received"]
        amount_received2=str(amount_received)
        
        
        if status == "succeeded" and amount_received != 0:
            print("a")
            if description == "Payment for Invoice":
                print("a")
                if amount_received==0:
                    pass
                else:
                    pass
        
                numara=id_checker_invoice(odeme)
                numara=str(numara)
                Fatura_text=invoice(fatura)
                Fatura_text="\n"+Fatura_text+","+numara
                
                if Fatura_text==data:
                    time.sleep(2)
                else:
                    
                    
                    webhook = DiscordWebhook(url='discord example webhook link')
                    embed = DiscordEmbed(title='Product and customer mail:', description=zaman+"\n"+Fatura_text+"\n"+amount_received2, color='03b2f8', rate_limit_retry=True)
                    
                    webhook.add_embed(embed)
                    response = webhook.execute()
                    

                    dosya=open("steamidcalisma.txt","w",encoding="utf8")
                    dosya.write(Fatura_text)
                    dosya.close()

                    dosya2=open("Orders.txt","a",encoding="utf8") #Loger
                    dosya2.write(zaman)
                    dosya2.write(" ")
                    dosya2.write(Fatura_text)
                    dosya2.write("\n")
                    dosya2.write("Previous data:")
                    dosya2.write(data)
                    dosya2.write("\n")
                    dosya2.close()
                    time.sleep(2)
            else:
                Odemeli_text=payment(odeme)
                numara=id_checker_payment(odeme)
                numara=str(numara)
                Odemeli_text="\n"+Odemeli_text+","+numara
                
                if Odemeli_text==data:
                    time.sleep(2)
                
                else:
                    webhook = DiscordWebhook(url='discord example webhook link')
                    embed = DiscordEmbed(title='Product and customer mail:', description=zaman+"\n"+Odemeli_text+"\n"+amount_received2, color='03b2f8', rate_limit_retry=True)
                    
                    webhook.add_embed(embed)
                    response = webhook.execute()

                    dosya=open("steamidcalisma.txt","w",encoding="utf8") 
                    dosya.write(Odemeli_text)
                    dosya.close()

                    dosya2=open("Orders.txt","a",encoding="utf8") 
                    dosya2.write(zaman)
                    dosya2.write(" ")

                    dosya2.write(Odemeli_text)
                    dosya2.write("\n")

                    dosya2.write("Previous data:")
                    dosya2.write(data)

                    dosya2.write("\n")
                    dosya2.close()

                    time.sleep(2)

        else:
            time.sleep(2)
           
    
    
    except Exception as error:
        error=str(error)
        errorfile=open("ErrorLog.txt","a",encoding="utf8")
        errorfile.write(zaman)
        errorfile.write("\n")
        errorfile.write(error)
        errorfile.write("\n")
        errorfile.close()
        time.sleep(2)