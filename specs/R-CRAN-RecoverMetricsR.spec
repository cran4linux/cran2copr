%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RecoverMetricsR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantifying Post-Fire Spectral Recovery Metrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.8
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-terra >= 1.8
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Computes pixel-wise metrics describing post-disturbance spectral recovery
from a yearly spectral-index time series. Metrics include disturbance
magnitude (DM), an ordinary least squares (OLS) recovery slope, early- and
late-period recovery rates, recovery-rate change, Relative Recovery
Indicator (RRI), Ratio of Eighty Percent (R80P), and Year-on-Year recovery
(YrYr). The RRI, R80P, and YrYr metrics are based on approaches described
by Frazier et al. (2018) <doi:10.1016/j.rse.2017.11.007>. Threshold-based
recovery-time approaches have been used to quantify post-fire vegetation
recovery from spectral time series by Chompuchan and Lin (2017)
<doi:10.1016/j.ecolind.2017.04.038>. Exponential recovery formulations
have also been applied to post-fire vegetation time series by Gouveia et
al. (2010) <doi:10.5194/nhess-10-673-2010>. Parametric recovery models,
including exponential, logistic, and Gompertz formulations, are provided
to characterize nonlinear post-disturbance recovery trajectories.

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
