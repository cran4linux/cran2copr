%global __brp_check_rpaths %{nil}
%global packname  onlineforecast
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Forecast Modelling for Online Applications

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-splines >= 3.1.1
BuildRequires:    R-CRAN-R6 >= 2.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-pbs 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-splines >= 3.1.1
Requires:         R-CRAN-R6 >= 2.2.2
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-pbs 
Requires:         R-CRAN-digest 

%description
A framework for fitting adaptive forecasting models. Provides a way to use
forecasts as input to models, e.g. weather forecasts for energy related
forecasting. The models can be fitted recursively and can easily be setup
for updating parameters when new data arrives. See the included vignettes,
the website <https://onlineforecasting.org> and the pre-print paper
"onlineforecast: An R package for adaptive and recursive forecasting"
<arXiv:2109.12915>.

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
