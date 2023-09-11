
import random
import smtplib

random_quote = ""
my_mail = "aryadevesh78@gmail.com"
password = "ysbihbwegocrmnma"

with open("quotes.txt", "r") as file:
    quotes = [quote for quote in file.readlines()]


def random_selection():
    global random_quote
    random_quote = random.choice(quotes)


random_selection()
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_mail, password)
    connection.sendmail(from_addr=my_mail,
                        to_addrs="agrawalpratibha096@gmail.com",
                        msg="Subject:Love Dose Everyday\n\nHello Bubu,\n"
                            "Some beautiful lines for the most beautiful girl  in the world.\n"
                            f" Motivational quote: {random_quote}\n. Always be happy and motivated <3."
                            "Byeee Love Take care :)"
                        )
