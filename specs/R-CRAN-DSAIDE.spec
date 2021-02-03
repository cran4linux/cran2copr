%global packname  DSAIDE
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamical Systems Approach to Infectious Disease Epidemiology (Ecology/Evolution)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98
BuildRequires:    R-utils >= 3.4
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-adaptivetau >= 2.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-shiny >= 1.2
BuildRequires:    R-CRAN-deSolve >= 1.13
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-lhs >= 0.15
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-XML >= 3.98
Requires:         R-utils >= 3.4
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-adaptivetau >= 2.2
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-shiny >= 1.2
Requires:         R-CRAN-deSolve >= 1.13
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-lhs >= 0.15
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Exploration of simulation models (apps) of various infectious disease
transmission dynamics scenarios. The purpose of the package is to help
individuals learn about infectious disease epidemiology
(ecology/evolution) from a dynamical systems perspective. All apps include
explanations of the underlying models and instructions on what to do with
the models.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
