%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rbeast
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
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
BEAST is a Bayesian estimator of abrupt change, seasonality, and trend for
decomposing univariate time series and 1D sequential data. Interpretation
of time series depends on model choice; different models can yield
contrasting or contradicting estimates of patterns, trends, and
mechanisms. BEAST alleviates this by abandoning the single-best-model
paradigm and instead using Bayesian model averaging over many competing
decompositions. It detects and characterizes abrupt changes (changepoints,
breakpoints, structural breaks, joinpoints), cyclic or seasonal variation,
and nonlinear trends. BEAST not only detects when changes occur but also
quantifies how likely the changes are true. It estimates not just
piecewise linear trends but also arbitrary nonlinear trends. BEAST is
generically applicable to any real-valued time series, such as those from
remote sensing, economics, climate science, ecology, hydrology, and other
environmental and biological systems. Example applications include
identifying regime shifts in ecological data, mapping forest disturbance
and land degradation from satellite image time series, detecting market
trends in economic indicators, pinpointing anomalies and extreme events in
climate records, and analyzing system dynamics in biological time series.
Details are given in Zhao et al. (2019) <doi:10.1016/j.rse.2019.04.034>.

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
