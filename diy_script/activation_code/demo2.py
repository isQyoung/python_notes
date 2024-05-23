import random, string


def randomCode(string_length):
    # 定义字符串池包含大写字母、小写字母、数字
    letters_all = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # 创建空变量code,每次从字符串池中随机取一个字符，拼接到code，最后返回一个string_length位数的code
    code = ''
    for _ in range(string_length):
        letter = random.choice(letters_all)
        code += letter
    return code


def generateActivationCode(num, length):
    codeList = []
    for _ in range(num):
        code = randomCode(length)
        while code in codeList:
            code = randomCode()
        codeList.append(code)
    return codeList


if __name__ == '__main__':
    print("生成10个 30位数的激活码")
    print(generateActivationCode(20, 30))
