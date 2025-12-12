%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GACE
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Adaptive Capped Estimator for Time Series Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides deterministic forecasting for weekly, monthly, quarterly, and
yearly time series using the Generalized Adaptive Capped Estimator. The
method includes preprocessing for missing and extreme values, extraction
of multiple growth components (including long-term, short-term, rolling,
and drift-based signals), volatility-aware asymmetric capping, optional
seasonal adjustment via damped and normalized seasonal factors, and a
recursive forecast formulation with moderated growth. The package includes
a user-facing forecasting interface and a plotting helper for
visualization. Related forecasting background is discussed in Hyndman and
Athanasopoulos (2021) <https://otexts.com/fpp3/> and Hyndman and Khandakar
(2008) <doi:10.18637/jss.v027.i03>. The method extends classical
extrapolative forecasting approaches and is suited for operational and
business planning contexts where stability and interpretability are
important.

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
