%global packname  MAINT.Data
%global packver   2.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model and Analyse Interval Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-sn >= 1.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.500.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-miscTools 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-sn >= 1.3.0
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-miscTools 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-withr 

%description
Implements methodologies for modelling interval data by Normal and
Skew-Normal distributions, considering appropriate parameterizations of
the variance-covariance matrix that takes into account the intrinsic
nature of interval data, and lead to four different possible configuration
structures. The Skew-Normal parameters can be estimated by maximum
likelihood, while Normal parameters may be estimated by maximum likelihood
or robust trimmed maximum likelihood methods.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
