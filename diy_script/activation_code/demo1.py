import uuid


def generateActivationCode(num):
    codeList = []
    for _ in range(num):
        code = str(uuid.uuid4()).replace('-', '').upper()
        while code in codeList:
            code = str(uuid.uuid4()).replace('-', '').upper()
        codeList.append(code)

    return codeList


if __name__ == '__main__':
    print("用uuid生成10个激活码")
    print(generateActivationCode(10))
