%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dcorBSS
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Distance-Correlation Based Methods for Blind Source Separation and Dependence Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-dccpp 
BuildRequires:    R-CRAN-dHSIC 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-dccpp 
Requires:         R-CRAN-dHSIC 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-nloptr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
Independent component analysis based on distance correlation, including a
robust variant using the bowl transformation. The package provides
user-facing implementations of distance covariance and distance
correlation, including memory-efficient blockwise computations for large
data sets. It includes a sequential ICA estimator based on minimizing
distance correlation, as well as tools for analyzing serial dependence via
distance autocorrelation, dependograms, and permutation-based tests. In
addition, it provides functions for testing serial dependence based on
distance correlation and the Hilbert–Schmidt independence criterion. The
methodology is related to Matteson and Tsay (2017)
<doi:10.1080/01621459.2016.1150851> and to the robust framework of Leyder
et al. (2026) <doi:10.1007/s11634-026-00674-9>.

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
