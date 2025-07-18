%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiLCIRT
%global packver   2.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.12
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Latent Class Item Response Theory Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-limSolve 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-limSolve 

%description
Framework for the Item Response Theory analysis of dichotomous and ordinal
polytomous outcomes under the assumption of multidimensionality and
discreteness of the latent traits. The fitting algorithms allow for
missing responses and for different item parameterizations and are based
on the Expectation-Maximization paradigm. Individual covariates affecting
the class weights may be included in the new version (since 2.1).

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
