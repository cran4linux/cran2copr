%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pmxNODE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Application of NODEs in 'Monolix', 'NONMEM', and 'nlmixr2'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-checkmate 

%description
An easy-to-use tool for implementing Neural Ordinary Differential
Equations (NODEs) in pharmacometric software such as 'Monolix', 'NONMEM',
and 'nlmixr2', see Bräm et al. (2024) <doi:10.1007/s10928-023-09886-4> and
Bräm et al. (2025) <doi:10.1002/psp4.13265>. The main functionality is to
automatically generate structural model code describing computations
within a neural network. Additionally, parameters and software settings
can be initialized automatically. For using these additional
functionalities with 'Monolix', 'pmxNODE' interfaces with 'MonolixSuite'
via the 'lixoftConnectors' package. The 'lixoftConnectors' package is
distributed with 'MonolixSuite'
(<https://monolixsuite.slp-software.com/r-functions/2024R1/package-lixoftconnectors>)
and is not available from public repositories.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
