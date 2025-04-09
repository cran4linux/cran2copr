%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rfast2
%global packver   0.1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Efficient and Extremely Fast R Functions II

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rnanoflann 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-zigg 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rnanoflann 

%description
A collection of fast statistical and utility functions for data analysis.
Functions for regression, maximum likelihood, column-wise statistics and
many more have been included. C++ has been utilized to speed up the
functions. References: Tsagris M., Papadakis M. (2018). Taking R to its
limits: 70+ tips. PeerJ Preprints 6:e26605v1
<doi:10.7287/peerj.preprints.26605v1>.

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
