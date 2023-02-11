import os,sys,win32api

def main():
    try:
        n = input("Target path: ")
        if not(os.path.exists(n)): sys.exit(1)
        s = input("Output path: ")
        file = bytearray(open(n, 'rb').read())
        sizet = os.path.getsize(n)
        with open(s, 'w') as output:
            output.write(f"char ByteArray[{sizet}] = ")
            output.write("{\n")
            for count, byte in enumerate(file, 1):
                output.write(f'{byte ^ ord("123"[(count - 1) % len("123")]):#0{4}x},' + ('\n' if not count % 16 else ' '))
            output.write("};")
    except Exception as ex:
        print("[ERROR] ",ex)
        sys.exit(1)

if __name__ == '__main__':
    main()