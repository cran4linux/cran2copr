%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iClick
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          A Button-Based GUI for Financial and Economic Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-fPortfolio 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-coefplot 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-JFE 
BuildRequires:    R-CRAN-FRAPO 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openair 
BuildRequires:    R-CRAN-papeR 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-fPortfolio 
Requires:         R-tcltk 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-car 
Requires:         R-CRAN-coefplot 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-forecast 
Requires:         R-grid 
Requires:         R-CRAN-JFE 
Requires:         R-CRAN-FRAPO 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-openair 
Requires:         R-CRAN-papeR 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
A GUI designed to support the analysis of financial-economic time series
data.

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
