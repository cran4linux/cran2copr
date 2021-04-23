%global packname  qrandom
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
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

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
