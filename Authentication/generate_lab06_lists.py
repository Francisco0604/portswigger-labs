a = 'carlos'
b = 'wiener'
y = 'peter'

with open('pass.txt', 'r') as f:
    x = [line.strip() for line in f if line.strip()]

usernames = []
passwords = []

count = 0
for pwd in x:
    usernames.append(a)
    passwords.append(pwd)
    count += 1
    if count % 2 == 0:
        usernames.append(b)
        passwords.append(y)

with open('usernames.txt', 'w') as f:
    f.write('\n'.join(usernames) + '\n')

with open('passwords.txt', 'w') as f:
    f.write('\n'.join(passwords) + '\n')

print(f"done! total entries: {len(usernames)}")
