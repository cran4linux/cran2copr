%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsem
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Structural Equation Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RTMB >= 1.7
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-sem 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-RTMB >= 1.7
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-sem 
Requires:         R-CRAN-igraph 
Requires:         R-utils 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-stats 

%description
Applies dynamic structural equation models to time-series data with
generic and simplified specification for simultaneous and lagged effects.
Methods are described in Thorson et al. (2024) "Dynamic structural
equation models synthesize ecosystem dynamics constrained by ecological
mechanisms."

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
