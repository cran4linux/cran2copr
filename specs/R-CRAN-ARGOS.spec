%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ARGOS
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Regression for Governing Equations (ARGOS)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-signal 
Requires:         R-parallel 
Requires:         R-CRAN-deSolve 

%description
Comprehensive set of tools for performing system identification of both
linear and nonlinear dynamical systems directly from data. The Automatic
Regression for Governing Equations (ARGOS) simplifies the complex task of
constructing mathematical models of dynamical systems from observed input
and output data, supporting various types of systems, including those
described by ordinary differential equations. It employs optimal numerical
derivatives for enhanced accuracy and employs formal variable selection
techniques to help identify the most relevant variables, thereby enabling
the development of predictive models for system behavior analysis.

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
