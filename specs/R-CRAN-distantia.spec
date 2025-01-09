%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  distantia
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Toolset for Efficient Time Series Dissimilarity Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-progressr 

%description
Fast C++ implementation of Dynamic Time Warping for time series
dissimilarity analysis, with applications in environmental monitoring and
sensor data analysis, climate science, signal processing and pattern
recognition, and financial data analysis. Built upon the ideas presented
in Benito and Birks (2020) <doi:10.1111/ecog.04895>, provides tools for
analyzing time series of varying lengths and structures, including
irregular multivariate time series. Key features include individual
variable contribution analysis, restricted permutation tests for
statistical significance, and imputation of missing data via GAMs.
Additionally, the package provides an ample set of tools to prepare and
manage time series data.

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
