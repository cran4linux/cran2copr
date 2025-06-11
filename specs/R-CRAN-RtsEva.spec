%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RtsEva
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Performs the Transformed-Stationary Extreme Values Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-POT 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-texmex 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-changepoint 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-POT 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-texmex 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-xts 
Requires:         R-grDevices 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-changepoint 

%description
Adaptation of the 'Matlab' 'tsEVA' toolbox developed by Lorenzo Mentaschi
available here: <https://github.com/menta78/tsEva>. It contains an
implementation of the Transformed-Stationary (TS) methodology for
non-stationary extreme value Analysis (EVA) as described in Mentaschi et
al. (2016) <doi:10.5194/hess-20-3527-2016>. In synthesis this approach
consists in: (i) transforming a non-stationary time series into a
stationary one to which the stationary extreme value theory can be
applied; and (ii) reverse-transforming the result into a non-stationary
extreme value distribution. 'RtsEva' offers several options for trend
estimation (mean, extremes, seasonal) and contains multiple plotting
functions displaying different aspects of the non-stationarity of
extremes.

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
