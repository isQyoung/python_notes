import struct
import hashlib


def uleb128_encode(value):
    """使用无符号 LEB128 编码整数"""
    result = []
    while value > 0x7F:
        result.append((value & 0x7F) | 0x80)
        value >>= 7
    result.append(value)
    return bytearray(result)


def get_challenge_bytes(challenge_objectid, challenge_str, challenge_difficulity, challenge_ture_num):
    """获取challenge bytes, 等于move中bcs::to_bytes()"""
    # 序列化 id 字段 (32 字节),跳过0x
    id_serialized = bytes.fromhex(challenge_objectid[2:])
    # 序列化 str 字段
    str_length_encoded = uleb128_encode(len(challenge_str))
    str_serialized = str_length_encoded + challenge_str.encode('utf-8')
    # 序列化 difficulity 和 ture_num 字段 (8 字节)
    difficulity_serialized = struct.pack('<Q', challenge_difficulity)
    ture_num_serialized = struct.pack('<Q', challenge_ture_num)
    # 合并所有字段的序列化结果转换成整数数组
    flag_str_serialized = id_serialized + str_serialized + difficulity_serialized + ture_num_serialized
    serialized_array = list(flag_str_serialized)
    # 输出序列化的整数数组
    print(len(serialized_array))  # 输出长度
    print(serialized_array)  # 输出内容

    return serialized_array


def generate_proof(challenge_bytes, sender_address, challenge_difficulty):
    "通过枚举获取匹配的proof"
    EPROOF = 0
    # 转为二进制对象
    challenge_bytes = bytearray(challenge_bytes)
    sender_bytes = bytes.fromhex(sender_address[2:])  # 跳过 '0x'

    # 定义“proof”字节数组（你需要找到正确的proof字节）
    proof = bytearray([0] * challenge_difficulty)  # 初始化proof数组为[0,0,0]
    for i in range(256):
        proof[0] = i
        for j in range(256):
            proof[1] = j
            for k in range(256):
                proof[2] = k
                # print(proof)
                full_proof = proof + sender_bytes + challenge_bytes
                hash_bytes = hashlib.sha3_256(full_proof).digest()
                prefix_sum = sum(hash_bytes[:challenge_difficulty])
                # print(prefix_sum)
                if prefix_sum == EPROOF:
                    return list(proof)

    return None


if __name__ == '__main__':
    sender_address = '0x741a3483255771b31d81d52b2018d6d69c739ec49f3077dadda93414825baa1b'
    challenge_objectid = '0xcd9aa0c7d6ee64b4de4de6a1ecf9cf84417c6cb5e5357935ba359e327cd9efe8'
    challenge_str = 'LetsMoveCTF'
    challenge_difficulity = 3
    challenge_ture_num = 0
    challenge_bytes = get_challenge_bytes(challenge_objectid, challenge_str, challenge_difficulity, challenge_ture_num)
    print(challenge_bytes)
    proof = generate_proof(challenge_bytes, sender_address, challenge_difficulity)
    print(proof)
