%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aedseo
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated and Early Detection of Seasonal Epidemic Onset and Burden Levels

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-base 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 

%description
A powerful tool for automating the early detection of seasonal epidemic
onsets in time series data. It offers the ability to estimate growth rates
across consecutive time intervals, calculate the sum of cases (SoC) within
those intervals, and estimate seasonal onsets within user defined seasons.
With use of a disease-specific threshold it also offers the possibility to
estimate seasonal onset of epidemics. Additionally it offers the ability
to estimate burden levels for seasons based on historical data. It is
aimed towards epidemiologists, public health professionals, and
researchers seeking to identify and respond to seasonal epidemics in a
timely fashion.

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
