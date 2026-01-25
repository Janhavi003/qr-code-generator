import qrcode

def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    user_data = input("Enter text or URL: ")
    generate_qr(user_data)
