import hashlib
from math import gcd

# ----------------------------
# 1. Генерация ключей
# ----------------------------

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17

assert gcd(e, phi) == 1

# d * e ≡ 1 (mod phi)
d = pow(e, -1, phi)

print("Публичный ключ :", (e, n))
print("Приватный ключ :", (d, n))

# ----------------------------
# 2. Сообщение
# ----------------------------

message = "f"

# SHA-256
hash_bytes = hashlib.sha256(message.encode()).digest()

# Байты -> число
hash_int = int.from_bytes(hash_bytes, "big")

print("\nХэш как число:")
print(hash_int)

# ----------------------------
# 3. Подпись
# ----------------------------

signature = pow(hash_int, d, n)

print("\nПодпись:")
print(signature)

# ----------------------------
# 4. Проверка подписи
# ----------------------------

recovered = pow(signature, e, n)

expected = hash_int % n

print("\nПолучили после проверки:")
print(recovered)

print("\nОжидали:")
print(expected)

print("\nПодпись верна:", recovered == expected)
