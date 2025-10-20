quote = '  "A room without books is like a body without a soul."  '
name = " marcus tullius cicero "
message = f'{name.title()}, one said:\n\t{quote}'
print(message)

message = f'{name.title().strip()}, one said:\n\t{quote.strip()}'
print(message)

message = f'{name.title().rstrip()}, one said:\n\t{quote.rstrip()}'

print(message)

message = f'{name.title().lstrip()}, one said:\n\t{quote.lstrip()}'

print(message)