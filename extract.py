import argparse
import oead

def extract_data(decompress,strap_arc_file, main_dol_file="main.dol", start_offset=3478400, expected_size=132351):
    try:
        with open(main_dol_file, 'rb') as main_dol:
            main_dol.seek(start_offset)
            data = main_dol.read(expected_size)
            if(decompress):
                data = oead.yaz0.decompress(data)

        with open(strap_arc_file, 'wb') as output:
            output.write(data)

        print("Data extracted and saved successfully to", strap_arc_file)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract data from 'main.dol'.")
    parser.add_argument("strap_arc_file", help="Path to the '.arc' file.")
    parser.add_argument("-no_decompress", "-ndc" ,help="Disables Yaz0 decompression", action='store_true')
    args = parser.parse_args()
    extract_data(not args.no_decompress,args.strap_arc_file)
