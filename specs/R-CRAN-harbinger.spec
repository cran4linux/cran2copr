%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  harbinger
%global packver   1.0.787
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.787
Release:          1%{?dist}%{?buildtag}
Summary:          A Unified Time Series Event Detection Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-daltoolbox 
BuildRequires:    R-CRAN-tsmp 
BuildRequires:    R-CRAN-dtwclust 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-wavelets 
BuildRequires:    R-CRAN-hht 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-daltoolbox 
Requires:         R-CRAN-tsmp 
Requires:         R-CRAN-dtwclust 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-wavelets 
Requires:         R-CRAN-hht 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-dplyr 

%description
By analyzing time series, it is possible to observe significant changes in
the behavior of observations that frequently characterize events. Events
present themselves as anomalies, change points, or motifs. In the
literature, there are several methods for detecting events. However,
searching for a suitable time series method is a complex task, especially
considering that the nature of events is often unknown. This work presents
Harbinger, a framework for integrating and analyzing event detection
methods. Harbinger contains several state-of-the-art methods described in
Salles et al. (2020) <doi:10.5753/sbbd.2020.13626>.

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
