%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prototest
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Inference on Prototypes from Clusters of Features

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-CRAN-intervals 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-CRAN-intervals 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-glmnet 

%description
Procedures for testing for group-wide signal in clusters of variables.
Tests can be performed for single groups in isolation (univariate) or
multiple groups together (multivariate). Specific tests include the exact
and approximate (un)selective likelihood ratio tests described in Reid et
al (2015), the selective F test and marginal screening prototype test of
Reid and Tibshirani (2015). User may pre-specify columns to be included in
prototype formation, or allow the function to select them itself. A
mixture of these two is also possible. Any variable selection is accounted
for using the selective inference framework. Options for non-sampling and
hit-and-run null reference distributions.

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
