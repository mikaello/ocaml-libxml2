# OCaml Bindings to libxml2.

NB: This is a mirror of the project of _kyas_ at the University of Oslo:
https://folk.uio.no/kyas/creoltools/index.html

This packages aims at providing bindings to [libxml](http://xmlsoft.org/)
version 2.6 and later. One aim of these bindings is to be as source-code
compatible with F# as possible.

To compile and link against the bindings, you cam use, e.g.,

```shell
ocamlfind ocamlc -package libxml2 MyProgram.ml
```

## Build Requirements

In order to compile this package, you need a ocaml compiler, e.g., from
http://caml.inria.fr. Version 3.06 and later are known to work. Many Linux
distributions already provide ocaml, a.o. Fedora, Ubuntu, and Debian.

You need findlib for ocaml, available from http://www.ocaml-programming.de.

You need libxml2, version 2.6.16 or later, including its development files.
Almost all Linux distributions include this library, but you can obtain it from
http://xmlsoft.org.

You need libxslt, version 1.1.11 or later, including its development files.
Almost all Linux distributions include this library, but you can obtain it from
http://xmlsoft.org.

## Build Instructions

See the file [INSTALL](./INSTALL.md) for more detailed instructions. Usually,

```shell
./configure make all make install
```

will install the bindings. It will create a package libxml2.

## Known Issues

Ubuntu and Debian do not ship libxslt.m4 with its libxslt-dev package.
Therefore, rebuilding from the repository will fail with a complaint about the
macro `AM_PATH_XSLT` being undefined. The correct remedy would be to make Ubuntu
correct its package. As a workaround, however, you can try to download the
libxslt source code, extract it, and copy the missing file to
`/usr/share/aclocal`.

The ABI of different versions of OCaml are not compatible. If you upgrade your
OCaml distribution, remember to upgrade or recompile and reinstall this library.

Similarily, upgrades of Linux distributions can overwrite important
configuration information of ocamlfind, which may make a reinstall necessary.
