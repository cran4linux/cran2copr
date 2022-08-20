%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMOPI
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Risk Management and Optimization for Portfolio Investment

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-TTR 
BuildRequires:    R-CRAN-fPortfolio 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-timeDate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-TTR 
Requires:         R-CRAN-fPortfolio 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-timeDate 

%description
Provides functions for risk management and portfolio investment of
securities with practical tools for data processing and plotting.
Moreover, it contains functions which perform the COS Method, an option
pricing method based on the Fourier-cosine series (Fang, F. (2008)
<doi:10.1137/080718061>).

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
