import base58


# 把sol钱包私钥转化为base58的数组列表
def convert_list(private_key):
    a = base58.b58decode(private_key)
    return list(a)

# 把base58的数组列表转回sol钱包私钥
def convert_private_key(my_list):
    b = base58.b58encode(bytes(my_list))
    return b

if __name__ == '__main__':
    # 私钥转数组
    private_key = '43sUsxXaqFvmpdCCwTdEU9K7i4XTCVRZ69TUR7CKCLdKiSnWGnkTQmzj6Ju6VkU9zyErWoonMh9Ca1iS16Fp4YaW'
    print(private_key)
    my_list = convert_list(private_key)
    output = str(my_list).replace(' ', '')
    print(output)
    print(my_list)
    # 数组转私钥
    #my_list = [163,71,190,122,235,172,74,201,8,225,144,222,236,167,29,33,100,181,224,29,242,211,147,143,100,246,120,234,111,197,66,218,135,178,247,2,167,31,76,82,50,133,164,15,237,186,55,77,121,9,7,94,110,84,216,63,134,91,86,223,199,229,233,146]
    my_private_key = convert_private_key(my_list)
    print(my_private_key)


