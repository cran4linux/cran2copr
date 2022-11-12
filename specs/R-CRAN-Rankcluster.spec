%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rankcluster
%global packver   0.98.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.98.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Based Clustering for Multivariate Partial Ranking Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 

%description
Implementation of a model-based clustering algorithm for ranking data (C.
Biernacki, J. Jacques (2013) <doi:10.1016/j.csda.2012.08.008>).
Multivariate rankings as well as partial rankings are taken into account.
This algorithm is based on an extension of the Insertion Sorting Rank
(ISR) model for ranking data, which is a meaningful and effective model
parametrized by a position parameter (the modal ranking, quoted by mu) and
a dispersion parameter (quoted by pi). The heterogeneity of the rank
population is modelled by a mixture of ISR, whereas conditional
independence assumption is considered for multivariate rankings.

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
