%global debug_package %{nil}
%global cname OpenBUGS

Name:           openbugs
Version:        3.2.3
Release:        1%{?dist}%{?buildtag}
Summary:        Bayesian Updating with Gibbs Sampling

License:        GPLv3
URL:            https://github.com/jsta/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc, glibc-devel(x86-32), automake, autoconf

%description
OpenBUGS is a program that conducts Bayesian estimation via Gibbs Sampling.
It is a continuation of the WinBUGS project, which was a continuation of
the BUGS project.

%prep
%autosetup -p1
sed -i '/LDFLAGS =/d' src/Makefile.am
sed -i 's|$(LDFLAGS)|$(CFLAGS) $(LDFLAGS) -L ../lib -m32|' src/Makefile.am
autoreconf -f || automake --add-missing
autoreconf -f

%build
./configure --prefix=%{_prefix}
%make_build

%install
%make_install
mv %{buildroot}%{_docdir}/%{name}- %{buildroot}%{_docdir}/%{name}

%files
%{_bindir}/%{cname}
%{_bindir}/%{cname}Cli
%{_prefix}/lib/lib%{cname}.so
%{_mandir}/man1/%{cname}.1*
%{_docdir}/%{name}

%changelog
