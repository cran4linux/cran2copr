%global packname  sanitizers
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          C/C++ source code to trigger Address and Undefined BehaviourSanitizers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Recent gcc and clang compiler versions provide functionality to memory
violations and other undefined behaviour; this is often referred to as
"Address Sanitizer" (or SAN) and "Undefined Behaviour Sanitizer" (UBSAN).
The Writing R Extension manual describes this in some detail in Section
4.9.

This feature has to be enabled in the corresponding binary, eg in R, which
is somewhat involved as it also required a current compiler toolchain
which is not yet widely available, or in the case of Windows, not
available at all (via the common Rtools mechanism).

As an alternative, the pre-built Docker containers available via the
Docker Hub at
https://registry.hub.docker.com/u/eddelbuettel/docker-debian-r/ can be
used on Linux, and via boot2docker on Windows and OS X.

This package then provides a means of testing the compiler setup as the
known code failures provides in the sample code here should be detected
correctly, whereas a default build of R will let the package pass.

The code samples are based on the examples from the Address Sanitizer Wiki
at https://code.google.com/p/address-sanitizer/wiki/AddressSanitizer.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/testUsage.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
