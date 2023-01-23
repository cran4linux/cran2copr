%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rbeast
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Change-Point Detection and Time Series Decomposition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grid 

%description
Interpretation of time series data is affected by model choices. Different
models can give different or even contradicting estimates of patterns,
trends, and mechanisms for the same data--a limitation alleviated by the
Bayesian estimator of abrupt change,seasonality, and trend (BEAST) of this
package. BEAST seeks to improve time series decomposition by forgoing the
"single-best-model" concept and embracing all competing models into the
inference via a Bayesian model averaging scheme. It is a flexible tool to
uncover abrupt changes (i.e., change-points), cyclic variations (e.g.,
seasonality), and nonlinear trends in time-series observations. BEAST not
just tells when changes occur but also quantifies how likely the detected
changes are true. It detects not just piecewise linear trends but also
arbitrary nonlinear trends. BEAST is applicable to real-valued time series
data of all kinds, be it for remote sensing, economics, climate sciences,
ecology, and hydrology. Example applications include its use to identify
regime shifts in ecological data, map forest disturbance and land
degradation from satellite imagery, detect market trends in economic data,
pinpoint anomaly and extreme events in climate data, and unravel system
dynamics in biological data. Details on BEAST are reported in Zhao et al.
(2019) <doi:10.1016/j.rse.2019.04.034>.

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
