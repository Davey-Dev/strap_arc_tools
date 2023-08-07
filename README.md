# strap_arc_tools

strap_arc_tools is a set of tools designed to simplify the process of extracting and injecting the `strap.arc` file from Wii Sports' `main.dol` file.
Only requirement is to put the executable(s) in the same directory as your `main.dol`

## How to Use

### Extracting

```strap_extract.exe [-h] [-no_decompress] strap_arc_file```

Adding the `-no_decompress` flag will make it so that you are extracting the data without decompressing it from the Yaz0 format.

`strap_arc_file` can be any filename, although you should end it with `.arc` so you can actually open it.


### Injecting

```strap_inject.exe [-h] [-no_compress] strap_arc_file```

Adding the `-no_decompress` flag will make it so that you are injecting the data without compressing it into the Yaz0 format.

`strap_arc_file` should point to the file you are injecting.
