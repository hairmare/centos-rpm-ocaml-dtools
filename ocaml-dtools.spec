Name:     ocaml-dtools

Version:  0.3.2
Release:  1
Summary:  OCAML daemon tools
License:  GPLv2+
URL:      https://github.com/chambart/ocaml-dtools
Source0:  https://github.com/savonet/ocaml-dtools/releases/download/0.3.2/ocaml-dtools-0.3.2.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-bytes
BuildRequires: pcre-ocaml
Requires:      ocaml-bytes
Requires:      pcre-ocaml

%prep
%setup -q 

%build
./configure --prefix=%{_prefix}
make all

%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT$(ocamlfind printconf destdir)
install -d $OCAMLFIND_DESTDIR
make install

%files
/usr/lib64/ocaml/dtools/META
/usr/lib64/ocaml/dtools/dtools.a
/usr/lib64/ocaml/dtools/dtools.cma
/usr/lib64/ocaml/dtools/dtools.cmi
/usr/lib64/ocaml/dtools/dtools.cmx
/usr/lib64/ocaml/dtools/dtools.cmxa
/usr/lib64/ocaml/dtools/dtools.mli

%description
OCaml modules for writing daemons

%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version