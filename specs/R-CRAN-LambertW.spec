%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LambertW
%global packver   0.6.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Models to Analyze and Gaussianize Heavy-Tailed, Skewed Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-lamW >= 1.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-methods 
Requires:         R-CRAN-lamW >= 1.3.0
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 
Requires:         R-methods 

%description
Lambert W x F distributions are a generalized framework to analyze skewed,
heavy-tailed data. It is based on an input/output system, where the output
random variable (RV) Y is a non-linearly transformed version of an input
RV X ~ F with similar properties as X, but slightly skewed (heavy-tailed).
The transformed RV Y has a Lambert W x F distribution. This package
contains functions to model and analyze skewed, heavy-tailed data the
Lambert Way: simulate random samples, estimate parameters, compute
quantiles, and plot/ print results nicely. The most useful function is
'Gaussianize', which works similarly to 'scale', but actually makes the
data Gaussian. A do-it-yourself toolkit allows users to define their own
Lambert W x 'MyFavoriteDistribution' and use it in their analysis right
away.

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
