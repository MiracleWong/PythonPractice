import uuid
print(uuid.uuid1())
print(uuid.uuid4())
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org'))
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org'))
x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')
print(str(x))
print(x.bytes)
print(uuid.UUID(bytes=x.bytes))
