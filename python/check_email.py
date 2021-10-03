# проверка email на валидацию

email = input("Введите email : ")

if email.count("@") == 1 \
    and email[0] != "@" \
    and email.count(".") > 0 \
    and email.rfind(".") > email.find("@"):
    print("valid email")
else:
    print("wrong email")


