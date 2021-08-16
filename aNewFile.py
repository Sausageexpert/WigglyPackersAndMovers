import dropbox

#please?

class DustyOlBox:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        sausage = open(file_from, 'rb')
        dbx.files_upload(sausage.read(), file_to)
    
def main():
    access_token = 'sl.A2psamK7oFzF7fS9MdwBrssRcDaKq8PVH0zSvvI5h5RfmwyPBn3TNCB1QrXWTLOKHcWMQt9x5CuEbzL25LrE_xikhKQ6gkuqcqR9KId7eEBzDXZBfG2neTwYJenB8_Ky394_ouI'
    badlyTapedBox = DustyOlBox(access_token)
    file_from = input("Choose file to be wrapped in brown tape: ")
    file_to = input("It's the journey that counts, not the destination... so it doesn't matter ")
    badlyTapedBox.upload(file_from, file_to)
    print("Trust Wiggly Packers and Movers, the best (non cold-blooded) packers and movers around!")

main()