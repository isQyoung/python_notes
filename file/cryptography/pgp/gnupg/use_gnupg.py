import gnupg

gpg = gnupg.GPG()
input_data = gpg.gen_key_input(
    key_type="RSA",
    key_length=4096,
    name_real="Example Key",
    name_comment='Example comment',
    name_email='test@example.com',
    passphrase='test123'
)

print(input_data)