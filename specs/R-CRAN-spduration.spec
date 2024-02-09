%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spduration
%global packver   0.17.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.2
Release:          1%{?dist}%{?buildtag}
Summary:          Split-Population Duration (Cure) Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-separationplot 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-corpcor 
Requires:         R-graphics 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-separationplot 
Requires:         R-CRAN-xtable 

%description
An implementation of split-population duration regression models. Unlike
regular duration models, split-population duration models are mixture
models that accommodate the presence of a sub-population that is not at
risk for failure, e.g. cancer patients who have been cured by treatment.
This package implements Weibull and Loglogistic forms for the duration
component, and focuses on data with time-varying covariates. These models
were originally formulated in Boag (1949) and Berkson and Gage (1952), and
extended in Schmidt and Witte (1989).

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
