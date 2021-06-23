%global __brp_check_rpaths %{nil}
%global packname  bbdetection
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Identification of Bull and Bear States of the Market

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-ggplot2 

%description
Implements two algorithms of detecting Bull and Bear markets in stock
prices: the algorithm of Pagan and Sossounov (2002, <doi:10.1002/jae.664>)
and the algorithm of Lunde and Timmermann (2004,
<doi:10.1198/073500104000000136>). The package also contains functions for
printing out the dating of the Bull and Bear states of the market, the
descriptive statistics of the states, and functions for plotting the
results. For the sake of convenience, the package includes the monthly and
daily data on the prices (not adjusted for dividends) of the S&P 500 stock
market index.

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
