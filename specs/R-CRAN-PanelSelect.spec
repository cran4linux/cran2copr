%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PanelSelect
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Panel Sample Selection Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-PanelCount 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pbv 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-PanelCount 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pbv 

%description
Extends the Heckman selection framework to panel data with individual
random effects. The first stage models participation via a panel Probit
specification, while the second stage can take a panel linear, Probit,
Poisson, or Poisson log-normal form. Model details are provided in Bailey
and Peng (2025) <doi:10.2139/ssrn.5475626> and Peng and Van den Bulte
(2024) <doi:10.1287/mnsc.2019.01897>.

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
