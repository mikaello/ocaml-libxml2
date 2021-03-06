%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:		ocaml-libxml2
Version:	0.0i
Release:	1%{?dist}
Summary:	OCaml bindings for libxml2
URL:		http://heim.ifi.uio.no/~kyas/
Source:		http://heim.ifi.uio.no/~kyas/%{name}-%{version}.tar.bz2
License:	GPL
Packager:       Marcel Kyas <kyas@users.berlios.de>
Group:		Development/Other
Requires:	ocaml >= 3.06
Requires:	ocaml-findlib
BuildRequires:	ocaml >= 3.06
BuildRequires:	ocaml-findlib-devel
BuildRequires:	libxml2-devel >= 2.6.11
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
This package contains bindings to the libxml2 library for ocaml.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

%clean
test -z "${RPM_BUILD_ROOT}" || rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root)
%doc ChangeLog README
%{_libdir}/ocaml/libxml2
%if %opt
%exclude %{_libdir}/ocaml/libxml2/*.a
%exclude %{_libdir}/ocaml/libxml2/*.cmxa
%endif
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%defattr(-,root,root,-)
%doc README
%if %opt
%{_libdir}/ocaml/libxml2/*.a
%{_libdir}/ocaml/libxml2/*.cmxa
%endif


%changelog
* Wed May 14 2008 Marcel Kyas <marcel.kyas@googlemail.com> - 0.0g-1
- Updated to latest upstream release.

* Thu Feb 21 2008 Marcel Kyas <marcel.kyas@googlemail.com> - 0.0f-1
- Updated to latest upstream release.

* Tue Aug 21 2007 Marcel Kyas <marcel.kyas@googlemail.com> - 0.0e-1
- Updated to latest upstream release.

* Fri Aug 17 2007 Marcel Kyas <marcel.kyas@googlemail.com> - 0.0d-1
- Updated to latest upstream release.

* Tue Aug 14 2007 Marcel Kyas <marcel.kyas@googlemail.com> - 0.0c-1
- Updated to latest upstream release.

* Sat Jun 30 2007 Marcel Kyas <marcel.kyas@googlemail.com> - 0.0b-1
- Updated to latest upstream release.

* Fri Jun 29 2007 Marcel Kyas <marcel.kyas@googlemail.com> - 0.0a-1
- Initial version.
