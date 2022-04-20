%global __brp_check_rpaths %{nil}
%global packname  energy
%global packver   1.7-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.10
Release:          1%{?dist}%{?buildtag}
Summary:          E-Statistics: Multivariate Inference via the Energy of Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-gsl 
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-stats 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-gsl 

%description
E-statistics (energy) tests and statistics for multivariate and univariate
inference, including distance correlation, one-sample, two-sample, and
multi-sample tests for comparing multivariate distributions, are
implemented. Measuring and testing multivariate independence based on
distance correlation, partial distance correlation, multivariate
goodness-of-fit tests, k-groups and hierarchical clustering based on
energy distance, testing for multivariate normality, distance components
(disco) for non-parametric analysis of structured data, and other energy
statistics/methods are implemented.

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
