%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DChaos
%global packver   0.1-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Chaotic Time Series Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-sandwich 

%description
Chaos theory has been hailed as a revolution of thoughts and attracting
ever increasing attention of many scientists from diverse disciplines.
Chaotic systems are nonlinear deterministic dynamic systems which can
behave like an erratic and apparently random motion. A relevant field
inside chaos theory and nonlinear time series analysis is the detection of
a chaotic behaviour from empirical time series data. One of the main
features of chaos is the well known initial value sensitivity property.
Methods and techniques related to test the hypothesis of chaos try to
quantify the initial value sensitive property estimating the Lyapunov
exponents. The DChaos package provides different useful tools and
efficient algorithms which test robustly the hypothesis of chaos based on
the Lyapunov exponent in order to know if the data generating process
behind time series behave chaotically or not.

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
