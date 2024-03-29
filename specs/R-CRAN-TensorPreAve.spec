%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TensorPreAve
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rank and Factor Loadings Estimation in Time Series Tensor Factor Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-pracma 

%description
A set of functions to estimate rank and factor loadings of time series
tensor factor models. A tensor is a multidimensional array. To analyze
high-dimensional tensor time series, factor model is a major dimension
reduction tool. 'TensorPreAve' provides functions to estimate the rank of
core tensors and factor loading spaces of tensor time series. More
specifically, a pre-averaging method that accumulates information from
tensor fibres is used to estimate the factor loading spaces. The estimated
directions corresponding to the strongest factors are then used for
projecting the data for a potentially improved re-estimation of the factor
loading spaces themselves. A new rank estimation method is also
implemented to utilizes correlation information from the projected data.
See Chen and Lam (2023) <arXiv:2208.04012> for more details.

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
