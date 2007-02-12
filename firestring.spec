Summary:	FireString - string handling library
Summary(pl.UTF-8):   FireString - biblioteka obsługująca łańcuchy znakowe
Name:		firestring
Version:	0.1.23
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://messagewall.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	f5d1b6fedbbd4137483efb3864d772b6
URL:		http://messagewall.org/firestring.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfirestring is a string handling library that provides maximum
length aware string handling functions to programs. Several functions
provide saner interfaces than the standard libc functions.
libfirestring also provides functions that are in most libc's but not
provided for by POSIX, enabling programmers to write POSIX-compliant
code while using such safe functions (strcasecmp, strncasecmp,
snprintf).

%description -l pl.UTF-8
libfirestring to biblioteka obsługująca łańcuchy znakowe dostarczająca
funkcje obsługujące łańcuchy z kontrolą maksymalnej długości. Kilka
funkcji ma bardziej rozsądne interfejsy niż standardowe funkcje libc.
libfirestring dostarcza także funkcje, które są w większości libc, ale
nie są wymagane przez POSIX, co pozwala programistom pisać zgodny z
POSIX kod z użyciem tych bezpiecznych funkcji (strcasecmp,
strncasecmp, snprintf).

%package devel
Summary:	Header files for firestring library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki firestring
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for firestring library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki firestring.

%package static
Summary:	Static firestring library
Summary(pl.UTF-8):   Statyczna biblioteka firestring
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static firestring library.

%description static -l pl.UTF-8
Statyczna biblioteka firestring.

%prep
%setup -q -n %{name}

%build
# it's FireMake, not autoconf-generated configure
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
./configure

%{__make} \
	SHAREDFLAGS="-shared -Wl,-soname=libfirestring.so"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	INSTALL_USER="`id -u`" \
	INSTALL_GROUP="`id -g`"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libfirestring.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/firestring.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfirestring.a
