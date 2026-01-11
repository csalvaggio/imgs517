# greybody - Graybody Model and Radiometric Utilities

---

## Complete uninstall and reset

In order to do a complete uninstall and reset for this module in the local `site_packages`:

Go to the project root
``` bash
cd /Users/cnspci/Desktop/graybody
```

1) Uninstall
``` bash
python3 -m pip uninstall -y graybody
```

2) Reinstall (editable + dev extras)
``` bash
python3 -m pip install -U pip
python3 -m pip install -e ".[dev]"
```

3) Run pytest
``` bash
python3 -m pytest -v
```

###### Quick “did I install the right thing?” checks

Show the editable install location:
``` bash
python3 -m pip list -e | grep graybody
python3 -m pip show graybody
```
You should see something like this on the console:
``` console
graybody 0.1.0   /Users/cnspci/Desktop/graybody

Name: graybody
Version: 0.1.0
Summary: Graybody Model and Radiometric Utilities
Home-page: https://github.com/yourname/graybody
Author:
Author-email: Carl Salvaggio <cnspci@rit.edu>
License: MIT
Location: /opt/homebrew/lib/python3.14/site-packages
Editable project location: /Users/cnspci/Desktop/graybody
Requires: numpy, pydantic
Required-by:
```

Confirm import path:
``` bash
python3 -c "import graybody; print(graybody.__file__)"
```
You should see something pointing into your working tree, like:
``` console
/Users/cnspci/Desktop/graybody/graybody/__init__.py
```

---

## License

This project is licensed under the MIT License.  
Copyright (c) 2025 Carl Salvaggio.

See the [LICENSE](LICENSE) file for details.

---

## Contact

**Carl Salvaggio, Ph.D.**  
Email: carl.salvaggio@rit.edu

[Chester F. Carlson Center for Imaging Science](https://www.rit.edu/science/chester-f-carlson-center-imaging-science)  
[Rochester Institute of Technology](https://www.rit.edu)  
Rochester, New York 14623  
United States

