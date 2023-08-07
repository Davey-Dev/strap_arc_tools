# strap.arc tools

strap.arc tools is a set of tools designed to simplify the process of extracting and injecting the `strap.arc` file from Wii Sports' `main.dol` file.

Only requirement is to put the executable(s) in the same directory as your `main.dol` file.



## Extracting

```strap_extract.exe [-h] [-no_decompress] strap_arc_file```

Adding the `-no_decompress` flag will make it so that you are extracting the data without decompressing it from the Yaz0 format.

`strap_arc_file` can be any filename, although you should end it with `.arc` so you can actually open it.


## Injecting

```strap_inject.exe [-h] [-no_compress] strap_arc_file```

Adding the `-no_decompress` flag will make it so that you are injecting the data without compressing it into the Yaz0 format.

`strap_arc_file` should point to the file you are injecting.


## Tips for modifying the file.

By default, these tools DO decompress and compress the Yaz0 format. 

If you plan on using [Wexos Toolbox](https://wiki.tockdom.com/wiki/Wexos%27s_Toolbox) to modify the arc file, you should use the `no_decompress` and `no_compress` flags as that program handles decompression and compression.

If you plan on using the [CTools Pack](https://wiki.tockdom.com/wiki/CTools_Pack), you should not use these flags.

Regardless of which extraction method you choose above, I'd recommend extracting each tpl file and modifying them using [BrawlCrate](https://github.com/soopercool101/BrawlCrate).

## Special Thanks

[Andrew (Beta 64)](https://beta64.tv) for showcasing the initial method of extracting and replacing files.
