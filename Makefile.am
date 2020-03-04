## Makefile.am - Use automake to create Makefile.in
#
# This file is part of ocaml-libxml2
#
# Written and Copyright (c) 2007, 2008 by Marcel Kyas
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see
# <http://www.gnu.org/licenses/>.

# Findlib related
export OCAMLFIND_DESTDIR

# Work around the (somewhat braindead) interaction between ocamlfind install
# and autoconf.  Eventually, this will need a better solution.
DISTCHECK_CONFIGURE_FLAGS = 'OCAMLFIND_DESTDIR=$${DESTDIR}$${libdir}/ocaml'

# OCaml compilers.
OCAMLC			= $(OCAMLFIND) ocamlc
OCAMLCP			= $(OCAMLFIND) ocamlcp
OCAMLOPT		= $(OCAMLFIND) ocamlopt
OCAMLDEP		= $(OCAMLFIND) ocamldep
OCAMLDOC		= $(OCAMLFIND) ocamldoc

MOSTLYCLEANFILES	= *~ *.aux *.log
CLEANFILES		= *.cmi *.cmo *.cmx *.cma *.cmxa *.o *.tex \
			  dllocaml-libxml2.so libocaml-libxml2.a ocaml-libxml2.a
DISTCLEANFILES		= META ocaml-libxml2.spec
MAINTAINERCLEANFILES	= .depend Makefile.in configure Version.ml \
			  depcomp missing install-sh aclocal.m4

EXTRA_DIST		= .depend META.in ocaml-libxml2.spec.in \
			  ocaml-libxml2.spec

BUILT_SOURCES		= META

noinst_LIBRARIES	= libxml2_stubs.a

libxml2_stubs_a_SOURCES	= xml_helpers.c xml_helpers.h xmld_stubs.c \
			  xmlr_stubs.c xmlw_stubs.c \
			  Xml.ml XmlTextReader.ml XmlTextWriter.ml

libxml2_stubs_o		= xml_helpers.o xmld_stubs.o \
			  xmlr_stubs.o xmlw_stubs.o
libxml2_stubs_ml	= Xml.ml XmlTextReader.ml XmlTextWriter.ml
libxml2_stubs_cmi	= Xml.cmi XmlTextReader.cmi XmlTextWriter.cmi
libxml2_stubs_cmo	= Xml.cmo XmlTextReader.cmo XmlTextWriter.cmo
libxml2_stubs_cmx	= Xml.cmx XmlTextReader.cmx XmlTextWriter.cmx

AM_CPPFLAGS		= $(XML_CPPFLAGS) $(XSLT_CPPFLAGS) -I`ocamlc -where` \
			  -DCAML_NAME_SPACE


# This probably works only with gcc.  It is not clear how we should handle
# position independend code (PIC) in a portable manner.
#
# i386 does not seem to have the stubs compiled as PIC.
# x86_64 insists on having PIC and accepts both -fpic and -fPIC
# Darwin wants us to use -fPIC only and wanrs about -fpic
# Solaris, HP-UX and others accept -fpic and -fPIC, but will use a
# small table with -fpic, which they prefer.

AM_CFLAGS		= -fPIC -DPIC

OCAMLC_FLAGS		= -I . -I ${srcdir} -g -w y
OCAMLOPT_FLAGS		= -I . -I ${srcdir} -w a

all-local: libocaml-xml2.cma libocaml-xml2.cmxa libocaml-libxml2.a

.PRECIOUS: *.cmo *.cmi *.cmx *.cma *.cmxa
.ml.cmo:
	$(OCAMLC) $(OCAMLC_FLAGS) -o $@ -c $<

.mli.cmi:
	$(OCAMLC) $(OCAMLC_FLAGS) -o $@ -c $<

.ml.cmx:
	$(OCAMLOPT) $(OCAMLOPT_FLAGS) -o $@ -c $<

# This builds the native archives.  dlllibxml2.so will be build as a
# side-effect of this rule, but building dlllibxml2.so is not always
# supported, therefore we do not depend on it.
libocaml-libxml2.a: $(libxml2_stubs_o)
	$(OCAMLMKLIB) -o ocaml-libxml2 $^ $(XML_LIBS)

libocaml-xml2.cma: $(libxml2_stubs_cmo)
	$(OCAMLMKLIB) -o ocaml-libxml2 $^ $(XML_LIBS)

libocaml-xml2.cmxa: $(libxml2_stubs_cmx)
	$(OCAMLMKLIB) -o ocaml-libxml2 $^ $(XML_LIBS)

META: $(srcdir)/META.in $(top_srcdir)/configure.ac
	rm -f META && sed -e s/@VERSION\@/$(VERSION)/g < $< > $@

.depend: $(oclvp_SOURCES) ${srcdir}/Makefile.am
	$(OCAMLDEP) $(OCAMLDEP_FLAGS) $(libxml2_stubs_ml) > $@

distclean-local:
	test ! -d html || rm -rf html

# We try hard to install the library, but this solution will fail with
# make distcheck.
install-exec-hook: META ocaml-libxml2.cma ocaml-libxml2.cmxa libocaml-libxml2.a ocaml-libxml2.a \
		$(libxml2_stubs_cmi)
	test -z "${OCAMLFIND_DESTDIR}" || \
		test -d ${OCAMLFIND_DESTDIR}/stublibs || \
		mkdir -p ${OCAMLFIND_DESTDIR}/stublibs || :
	$(OCAMLFIND) install libxml2 $^ -optional -dll dllocaml-libxml2.so

uninstall-local:
	$(OCAMLFIND) remove libxml2

html-local: ${srcdir}/Makefile.am $(libxml2_stubs_ml)
	test ! -d html || rm -rf html
	mkdir html
	$(OCAMLDOC) $(OCAMLFIND_FLAGS) -html -d html -m A $(libxml2_stubs_ml)
	date > $@

XmlTextReader.cmi XmlTextWriter.cmi: META

ocaml-libxml2.spec: ${srcdir}/ocaml-libxml2.spec.in \
	${srcdir}/configure.ac
	sed "s/@VERSION\@/${VERSION}/" < $< > $@

-include ${srcdir}/.depend
