import dis

# dis.disassemble_file(open('example.pyc', 'rb'))

# uncompyle6 -o . /path/to/your/file.pyc
# uncompyle6 -o . /Users/li/Downloads/fields.pyc


import dis

with open("/Users/li/Downloads/fields.pyc", "rb") as f:
    code = f.read()
    print(code)
    # print(dis.dis(code))
