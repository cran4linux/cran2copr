%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  esemifar
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Smoothing Long-Memory Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-smoots 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-fracdiff 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-smoots 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-ggplot2 

%description
The nonparametric trend and its derivatives in equidistant time series
(TS) with long-memory errors can be estimated. The estimation is conducted
via local polynomial regression using an automatically selected bandwidth
obtained by a built-in iterative plug-in algorithm or a bandwidth fixed by
the user. The smoothing methods of the package are described in Letmathe,
S., Beran, J. and Feng, Y., (2023) <doi:10.1080/03610926.2023.2276049>.

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
