%global packname  qrandom
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}
Summary:          True Random Numbers using the ANU Quantum Random Numbers Server

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-Rmpfr 
Requires:         R-utils 

%description
The ANU Quantum Random Number Generator provided by the Australian
National University generates true random numbers in real-time by
measuring the quantum fluctuations of the vacuum. This package offers an
interface using their API. The electromagnetic field of the vacuum
exhibits random fluctuations in phase and amplitude at all frequencies. By
carefully measuring these fluctuations, one is able to generate ultra-high
bandwidth random numbers. The quantum Random Number Generator is based on
the papers by Symul et al., (2011) <doi:10.1063/1.3597793> and Haw, et al.
(2015) <doi:10.1103/PhysRevApplied.3.054004>. The package offers functions
to retrieve a sequence of random integers or hexadecimals and true random
samples from a normal or uniform distribution.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
