# strap.arc tools

strap.arc tools is a set of tools designed to simplify the process of extracting and injecting the `strap.arc` file from Wii Sports' `main.dol` file.

For those unaware, strap.arc is the file responsible for the initial Wii Remote Strap warning screen when you load up Wii Sports.

Only requirement for using this tool is to put the executable(s) in the same directory as your `main.dol` file.



## Extracting

```strap_extract.exe [-h] [-no_decompress] strap_arc_file```

Adding the `-no_decompress` flag will make it so that you are extracting the data without decompressing it from the Yaz0 format.

`strap_arc_file` can be any filename, although you should end it with `.arc` so you can actually open it.


## Injecting

```strap_inject.exe [-h] [-no_compress] strap_arc_file```

Adding the `-no_decompress` flag will make it so that you are injecting the data without compressing it into the Yaz0 format.

`strap_arc_file` should point to the file you are injecting.


## Tips for Modification

I have written a full text guide on how to use this tool alongside other tools in order to replace textures and have them appear in-game. That guide can be found [here](https://docs.google.com/document/d/1l55WSyeNgI1XAzLc_PVrlI4oAwe5Qf6TACvlAqcS_UQ/edit?usp=sharing).

[Andrew (Beta 64)](https://beta64.tv) has a video of his stream highlights where he used Wexos Toolbox and BrawlCrate. That video can be found [here](https://youtu.be/xf76Ui_MsaI).

## Special Thanks

[Andrew (Beta 64)](https://beta64.tv) for showcasing the initial method of extracting and replacing files using HxD.
