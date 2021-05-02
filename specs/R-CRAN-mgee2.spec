%global packname  mgee2
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Marginal Analysis of Misclassified Longitudinal Ordinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 

%description
Three estimating equation methods are provided in this package for
marginal analysis of longitudinal ordinal data with misclassified
responses and covariates. The naive analysis which is solely based on the
observed data without adjustment may lead to bias. The corrected
generalized estimating equations (GEE2) method which is unbiased requires
the misclassification parameters to be known beforehand. The corrected
generalized estimating equations (GEE2) with validation subsample method
estimates the misclassification parameters based on a given validation
set. This package is an implementation of Chen (2013)
<doi:10.1002/bimj.201200195>.

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
