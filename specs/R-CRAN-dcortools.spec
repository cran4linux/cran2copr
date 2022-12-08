%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dcortools
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Providing Fast and Flexible Functions for Distance Correlation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 

%description
Provides methods for distance covariance and distance correlation
(Szekely, et al. (2007) <doi:10.1214/009053607000000505>), generalized
version thereof (Sejdinovic, et al. (2013) <doi:10.1214/13-AOS1140>) and
corresponding tests (Berschneider, Bottcher (2018) <arXiv:1808.07280>.
Distance standard deviation methods (Edelmann, et al. (2020)
<doi:10.1214/19-AOS1935>) and distance correlation methods for survival
endpoints (Edelmann, et al. (2021) <doi:10.1111/biom.13470>) are also
included.

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
