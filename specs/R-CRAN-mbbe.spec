%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mbbe
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model Based Bio-Equivalence

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-furrr >= 0.3.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-PKNCA 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ps 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-furrr >= 0.3.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-PKNCA 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-future 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ps 
Requires:         R-CRAN-jsonlite 

%description
Uses several Nonlinear Mixed effect (NONMEM) models (as NONMEM control
files) to perform bootstrap model averaging and Monte Carlo Simulation for
Model Based Bio-Equivalence (MBBE). Power is returned as the fraction of
the simulations with successful bioequivalence (BE) test, for maximum
concentration (Cmax), Area under the curve to the last observed value
(AUClast) and Area under the curve extrapolate to infinity (AUCinf). See
Hooker, A. (2020) Improved bioequivalence assessment through
model-informed and model-based strategies
<https://www.fda.gov/media/138035/download>.

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
