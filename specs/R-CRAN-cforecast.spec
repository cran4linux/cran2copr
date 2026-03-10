%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cforecast
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Forecasting and Scenario Analysis Using VAR Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BVAR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-FKF 
BuildRequires:    R-CRAN-miscTools 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-wex 
Requires:         R-CRAN-BVAR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-FKF 
Requires:         R-CRAN-miscTools 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vars 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-wex 

%description
Provides tools for conducting scenario analysis in reduced-form vector
autoregressive (VAR) models. Implements a Kalman filtering framework to
generate forecasts under path restrictions on selected variables. The
package enables decomposition of conditional forecasts into
variable-specific contributions, and extraction of observation weights. It
also computes measures of overall and marginal variable importance to
enhance the economic interpretation of forecast revisions. The framework
is structurally agnostic and suited for policy analysis, stress testing,
and macro-financial applications. The methodology is described in more
detail in Caspi and Ginker (2026) <doi:10.13140/RG.2.2.25225.51040>.

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
