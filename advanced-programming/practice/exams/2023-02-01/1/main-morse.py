from morse import Morse

if __name__ == "__main__":
    M = Morse()
    print(f"SOS SAVE THE DEVS CHATGPT RULEZ, \
            {M.encode('SOS SAVE THE DEVS CHATGPT RULEZ')}")
    print(f"....u.u._..u._..u___ .__u___u._.u._..u_.., \
            {M.decode('....u.u._..u._..u___ .__u___u._.u._..u_..')}")
