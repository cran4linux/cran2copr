%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesianNetwork
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Network Modeling and Analysis

License:          Apache License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-heatmaply 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-heatmaply 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 

%description
A "Shiny"" web application for creating interactive Bayesian Network
models, learning the structure and parameters of Bayesian networks, and
utilities for classic network analysis.

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
