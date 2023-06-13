%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seededlda
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Seeded Sequential LDA for Topic Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-quanteda >= 3.3.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.600.1.0
BuildRequires:    R-CRAN-proxyC >= 0.3.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-quanteda >= 3.3.0
Requires:         R-CRAN-proxyC >= 0.3.1
Requires:         R-methods 
Requires:         R-CRAN-Matrix 

%description
Seeded Sequential LDA can classify sentences of texts into pre-define
topics with a small number of seed words (Watanabe & Baturo, 2023)
<doi:10.1177/08944393231178605>. Implements Seeded LDA (Lu et al., 2010)
<doi:10.1109/ICDMW.2011.125> and Sequential LDA (Du et al., 2012)
<doi:10.1007/s10115-011-0425-1> with the distributed LDA algorithm
(Newman, et al., 2009) for parallel computing.

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
