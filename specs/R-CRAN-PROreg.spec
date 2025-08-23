%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PROreg
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Patient Reported Outcomes Regression Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-car 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Matrix 

%description
It offers a wide variety of techniques, such as graphics, recoding, or
regression models, for a comprehensive analysis of patient-reported
outcomes (PRO). Especially novel is the broad range of regression models
based on the beta-binomial distribution useful for analyzing binomial data
with over-dispersion in cross-sectional, longitudinal, or multidimensional
response studies (see Najera-Zuloaga J., Lee D.-J. and Arostegui I. (2019)
<doi:10.1002/bimj.201700251>).

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
