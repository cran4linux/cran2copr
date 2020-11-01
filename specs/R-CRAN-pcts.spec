%global packname  pcts
%global packver   0.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15
Release:          1%{?dist}%{?buildtag}
Summary:          Periodically Correlated and Periodically Integrated Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PolynomF >= 2.0.2
BuildRequires:    R-CRAN-Rdpack >= 0.9
BuildRequires:    R-CRAN-lagged >= 0.2.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sarima 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-gbutils 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-mcompanion 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-PolynomF >= 2.0.2
Requires:         R-CRAN-Rdpack >= 0.9
Requires:         R-CRAN-lagged >= 0.2.2
Requires:         R-methods 
Requires:         R-CRAN-sarima 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-gbutils 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-stats4 
Requires:         R-CRAN-mcompanion 
Requires:         R-CRAN-lubridate 

%description
Classes and methods for modelling and simulation of periodically
correlated (PC) and periodically integrated time series.  Compute
theoretical periodic autocovariances and related properties of PC
autoregressive moving average models. Some original methods including
Boshnakov & Iqelan (2009) <doi:10.1111/j.1467-9892.2009.00617.x>,
Boshnakov (1996) <doi:10.1111/j.1467-9892.1996.tb00281.x>.

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
