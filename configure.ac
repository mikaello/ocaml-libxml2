dnl configure.ac -- use autoconf to create configure from this file.
dnl
dnl This file is part of ocaml-libxml2 (OCaml bindings to libxml2)
dnl
dnl Written and Copyright (c) 2005, 2007, 2008 by Marcel Kyas
dnl
dnl This program is free software; you can redistribute it and/or
dnl modify it under the terms of the GNU General Public License as
dnl published by the Free Software Foundation; either version 3 of the
dnl License, or (at your option) any later version.
dnl
dnl This program is distributed in the hope that it will be useful, but
dnl WITHOUT ANY WARRANTY; without even the implied warranty of
dnl MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
dnl General Public License for more details.
dnl
dnl You should have received a copy of the GNU General Public License
dnl along with this program.  If not, see
dnl <http://www.gnu.org/licenses/>.

AC_INIT([ocaml-libxml2], [0.0i], [kyas@ifi.uio.no])
AC_PREREQ([2.59])
AC_CONFIG_SRCDIR([XmlTextWriter.ml])
AM_INIT_AUTOMAKE([1.9 dist-bzip2 readme-alpha check-news])

dnl Check for the tools needed to build the text-reader and text-writer
dnl libraries
AC_PROG_CC
AC_PROG_RANLIB
AM_PATH_XML2(2.6.16)

dnl Check for the tools needed to compile ocaml code.
AC_CHECK_PROG([OCAMLFIND], [ocamlfind], [ocamlfind], [false])
if test -z "$OCAMLFIND"
then
    AC_MSG_ERROR([ocamlfind is not installed.

You have to install findlib from <http://www.ocaml-programming.de/>
to compile the ocaml xml bindings.  Alternatively, you can install the
godi distribution from <http://godi.ocaml-programming.de/> to satisfy
this dependency.
])
fi

AC_CHECK_PROG([OCAMLMKLIB], [ocamlmklib], [ocamlmklib], [])
if test -z "$OCAMLMKLIB"
then
    AC_MSG_ERROR([ocamlmklib is not installed.

You have to install ocaml from <http://caml.inria.fr/>
to compile the ocaml xml bindings.  Alternatively, you can install the
godi distribution from <http://godi.ocaml-programming.de/> to satisfy
this dependency.
])
fi

AC_MSG_CHECKING([for ocaml-libxml2])
OCAML_LIBXML2_VERSION=`$OCAMLFIND query -format '%v' libxml2 2>/dev/null`
if test "$?" = "0"
then
  AC_MSG_RESULT($OCAML_LIBXML2_VERSION)
  AC_MSG_WARN([[It looks like you have an old version of ocaml-libxml
already installed.  You should run ``make uninstall'' to remove the old 
version before installing this version with ``make install''.]])
else
  AC_MSG_RESULT([no])
fi

AC_SUBST([OCAMLC_FLAGS])
AC_SUBST([OCAMLOPT_FLAGS])
OCAMLFIND_DESTDIR=${OCAMLFIND_DESTDIR:=""}
AC_SUBST([OCAMLFIND_DESTDIR])

AC_OUTPUT([Makefile])
