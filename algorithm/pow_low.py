import hashlib


def uleb128_encode(value):
    """使用无符号 LEB128 编码整数"""
    result = []
    while value > 0x7F:
        result.append((value & 0x7F) | 0x80)
        value >>= 7
    result.append(value)
    return bytearray(result)


def get_flag(flag_str, githubid):
    """使用FlagString中的str和githubid获取flag对应的数组"""
    str_length_encoded = uleb128_encode(len(flag_str))
    str_serialized = str_length_encoded + flag_str.encode('utf-8')
    github_bytes = bytes(githubid.encode())
    full_flag = str_serialized + github_bytes
    hash_bytes = hashlib.sha3_256(full_flag).digest()
    flag = list(hash_bytes)
    return flag


if __name__ == '__main__':
    flag_str = "LetsMoveCTF"
    githubid = "isQyoung"
    flag = get_flag(flag_str, githubid)
    print(flag)
