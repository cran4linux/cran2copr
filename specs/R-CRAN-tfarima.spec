%global packname  tfarima
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Transfer Function and ARIMA Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-zoo 

%description
Building customized transfer function and ARIMA models with multiple
operators and parameter restrictions. Functions for model identification,
model estimation (exact or conditional maximum likelihood), model
diagnostic checking, automatic outlier detection, calendar effects,
forecasting and seasonal adjustment. See Bell and Hillmer (1983)
<doi:10.1080/01621459.1983.10478005>, Box, Jenkins, Reinsel and Ljung
<ISBN:978-1-118-67502-1>, Box, Pierce and Newbold (1987)
<doi:10.1080/01621459.1987.10478430>, Box and Tiao (1975)
<doi:10.1080/01621459.1975.10480264>, Chen and Liu (1993)
<doi:10.1080/01621459.1993.10594321>, Thompson and Tiao (1970)
<http://old-www.stat.wisc.edu/sites/default/files/TR222.pdf>.

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
