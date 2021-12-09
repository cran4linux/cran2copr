%global __brp_check_rpaths %{nil}
%global packname  evolvability
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculation of Evolvability Parameters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-lme4 
Requires:         R-stats 

%description
Provides tools for calculating evolvability parameters from estimated
G-matrices as defined in Hansen and Houle (2008)
<doi:10.1111/j.1420-9101.2008.01573.x> and fits phylogenetic comparative
models that link the rate of evolution of a trait to the state of another
evolving trait (see Hansen et al. 2021 Systematic Biology
<doi:10.1093/sysbio/syab079>). The package was released with Bolstad et
al. (2014) <doi:10.1098/rstb.2013.0255>, which contains some examples of
use.

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
