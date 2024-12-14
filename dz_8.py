import  logging
logging.basicConfig(level=logging.DEBUG,filename="error_log.log",filemode="w",format="We have next loggingmessage:%(asctime)s:%(levelname)s -%(message)s")
logging.debug("Code started working")
first = int(input("Введите первое число: "))
logging.debug(f"User entered first number : {first}")
second = int(input("Введите второе число: "))
logging.debug(f"User entered second number: {second}")
if second // 1 > 0:
    logging.info("Second : Division is successful")
elif second // 1 == 0:
    logging.error("Second : User entered zero. Division is impossible.")
if first // 1 > 0:
    logging.info("First : Division is successful")
elif first // 1 == 0:
    logging.error("First : User entered zero. Division is impossible.")