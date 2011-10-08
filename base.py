# Converts decimal numbers to different bases

base = lambda num, b: (num == 0 and  "0" ) or ( base(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~`!@#$%^&*()_-+={[}]:;<,>.?/\"'\\|"[num % b])
