%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FoCo2
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Coherent Forecast Combination for Linearly Constrained Multiple Time Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-FoReco 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-osqp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-FoReco 
Requires:         R-stats 
Requires:         R-CRAN-cli 
Requires:         R-methods 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-osqp 

%description
Methods and tools designed to improve the forecast accuracy for a linearly
constrained multiple time series, while fulfilling the linear/aggregation
relationships linking the components (Girolimetto and Di Fonzo, 2024
<doi:10.48550/arXiv.2412.03429>). 'FoCo2' offers multi-task forecast
combination and reconciliation approaches leveraging input from multiple
forecasting models or experts and ensuring that the resulting forecasts
satisfy specified linear constraints. In addition, linear inequality
constraints (e.g., non-negativity of the forecasts) can be imposed, if
needed.

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
