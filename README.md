# strap_arc_tools

Both inject and extract take a single argument, the arc file you are either injecting to or extracting from.

Assuming you have main.dol in the same folder as this script, here's some examples.


```python inject.py idunno.arc```

- This injects the data from 'idunno.arc' into the section of 'main.dol' for the strap.arc data. The code automatically pads the extra 0s you may need if you are under file size of 132,351 bytes.

```python extract.py idunno.arc```

- This extracts the strap.arc data from 'main.dol' into 'idunno.arc', which you can then open with Wexos Toolkit and/or BrawlCrate.
