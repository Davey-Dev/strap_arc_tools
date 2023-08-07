import argparse
import oead

def inject_data(compress, strap_arc_file, main_dol_file="main.dol", start_offset=3478400, expected_size=132351):
    try:
        with open(main_dol_file, 'r+b') as main_dol, open(strap_arc_file, 'rb') as strap_arc:

            data_to_inject = strap_arc.read()
            if(compress):
                print("Size before compression: ", len(data_to_inject))
                data_to_inject = oead.yaz0.compress(data_to_inject)
                print("Size after compression: ", len(data_to_inject))
            else:
                print("Size: ", len(data_to_inject))
                
            if len(data_to_inject) == expected_size:
                main_dol.seek(start_offset)
                main_dol.write(data_to_inject)
                print("Data injected successfully.")
            elif len(data_to_inject) < expected_size:
                padding_size = expected_size - len(data_to_inject)
                padding_data = bytes([0] * padding_size)
                main_dol.seek(start_offset)
                main_dol.write(data_to_inject)
                main_dol.write(padding_data)
                print("Data injected with padding.")
            else:
                print("Injection canceled. 'strap.arc' size is greater than expected. (Needs to be less than 132351)")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inject data into 'main.dol'.")
    parser.add_argument("strap_arc_file", help="Path to the '.arc' file.")
    parser.add_argument("-no_compress", "-nc" ,help="Disables Yaz0 compression", action='store_true')
    args = parser.parse_args()
    inject_data(not args.no_compress,args.strap_arc_file)
