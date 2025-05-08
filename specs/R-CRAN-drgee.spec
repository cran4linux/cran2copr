%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drgee
%global packver   1.1.10-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.10.3
Release:          1%{?dist}%{?buildtag}
Summary:          Doubly Robust Generalized Estimating Equations

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 

%description
Fit restricted mean models for the conditional association between an
exposure and an outcome, given covariates. Three methods are implemented:
O-estimation, where a nuisance model for the association between the
covariates and the outcome is used; E-estimation where a nuisance model
for the association between the covariates and the exposure is used, and
doubly robust (DR) estimation where both nuisance models are used. In
DR-estimation, the estimates will be consistent when at least one of the
nuisance models is correctly specified, not necessarily both. For more
information, see Zetterqvist and Sjölander (2015)
<doi:10.1515/em-2014-0021>.

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
