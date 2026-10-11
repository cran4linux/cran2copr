%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  toeclim
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time of Emergence of Climate Signals from Internal Variability

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Detects when a forced climate change signal emerges from internal
variability ('time of emergence') in annual climate time series such as
temperature or precipitation. The signal is estimated with a linear,
quadratic or locally weighted smoother and compared with noise estimated
from a baseline period. Emergence is defined through configurable
signal-to-noise thresholds and persistence rules. Uncertainty in the time
of emergence is quantified by autoregressive or moving-block bootstrap
resampling. Helpers are provided for multi-member ensembles, threshold
sensitivity, anomaly and annual aggregation, Mann-Kendall trend tests with
trend-free prewhitening, and synthetic data generation. The approach
builds on Hawkins and Sutton (2012) <doi:10.1029/2011GL050087>, Yue et al.
(2002) <doi:10.1002/hyp.1095> and Sen (1968)
<doi:10.1080/01621459.1968.10480934>.

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
