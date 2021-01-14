%global packname  MGDrivE2
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mosquito Gene Drive Explorer 2

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-deSolve 

%description
A simulation modeling framework which significantly extends capabilities
from the 'MGDrivE' simulation package via a new mathematical and
computational framework based on stochastic Petri nets. For more
information about 'MGDrivE', see our publication:
<https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13318>.
Some of the notable capabilities of 'MGDrivE2' include: incorporation of
human populations, epidemiological dynamics, time-varying parameters, and
a continuous-time simulation framework with various sampling algorithms
for both deterministic and stochastic interpretations. 'MGDrivE2' relies
on the genetic inheritance structures provided in package 'MGDrivE', so we
suggest installing that package initially.

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
