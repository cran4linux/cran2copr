%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forecastADAPT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Adaptive Forecast

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-testcorr 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-lubridate 
Requires:         R-grDevices 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-testcorr 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
The function forAD() implements the adaptive forecasting procedure of
Giraitis, Kapetanios and Price (2013) <doi:10.1016/j.jeconom.2013.04.003>.
The method can be iterated (e.g., adapt²) and combined with autoregressive
(AR) forecasting. These approaches are computationally simple and adapt
automatically to structural changes without requiring prior specification
of the underlying data-generating process. They are applicable to both
stationary and non-stationary time series. The numerical and graphical
outputs assist in selecting an appropriate forecasting method,
particularly one that minimises mean squared forecast error (MSFE) and
yields uncorrelated forecast errors.

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
