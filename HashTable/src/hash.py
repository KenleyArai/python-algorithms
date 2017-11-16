class Hash:
    @staticmethod
    def encode_string(string_to_encode):
        return [ord(s) for s in string_to_encode]

    @staticmethod
    def hash(string_to_hash, mod):
        encoded_string = Hash.encode_string(string_to_hash)
        return sum(encoded_string) % mod
