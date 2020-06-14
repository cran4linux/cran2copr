%global packname  remoter
%global packver   0.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}
Summary:          Remote R: Control a Remote R Session from a Local One

License:          BSD 2-clause License + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pbdZMQ >= 0.3.0
BuildRequires:    R-CRAN-argon2 >= 0.2.0
BuildRequires:    R-CRAN-png >= 0.1.7
BuildRequires:    R-CRAN-getPass >= 0.1.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-pbdZMQ >= 0.3.0
Requires:         R-CRAN-argon2 >= 0.2.0
Requires:         R-CRAN-png >= 0.1.7
Requires:         R-CRAN-getPass >= 0.1.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
A set of utilities for client/server computing with R, controlling a
remote R session (the server) from a local one (the client).  Simply set
up a server (see package vignette for more details) and connect to it from
your local R session ('RStudio', terminal, etc).  The client/server
framework is a custom 'REPL' and runs entirely in your R session without
the need for installing a custom environment on your system.  Network
communication is handled by the 'ZeroMQ' library by way of the 'pbdZMQ'
package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
