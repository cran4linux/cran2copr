%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SKFCPD
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Online Changepoint Detection for Temporally Correlated Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods >= 4.2.2
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-FastGaSP >= 0.5.2
BuildRequires:    R-CRAN-ggpubr >= 0.5.0
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods >= 4.2.2
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-FastGaSP >= 0.5.2
Requires:         R-CRAN-ggpubr >= 0.5.0

%description
Sequential Kalman filter for scalable online changepoint detection by
temporally correlated data. It enables fast single and multiple change
points with missing values. See the reference: Hanmo Li, Yuedong Wang,
Mengyang Gu (2023), <arXiv:2310.18611>.

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
