%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Epi
%global packver   2.52
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.52
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis in Epidemiology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-CRAN-etm 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-cmprsk 
Requires:         R-CRAN-etm 
Requires:         R-splines 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-magrittr 

%description
Functions for demographic and epidemiological analysis in the Lexis
diagram, i.e. register and cohort follow-up data. In particular
representation, manipulation, rate estimation and simulation for
multistate data - the Lexis suite of functions, which includes interfaces
to 'mstate', 'etm' and 'cmprsk' packages. Contains functions for
Age-Period-Cohort and Lee-Carter modeling and a function for interval
censored data and some useful functions for tabulation and plotting, as
well as a number of epidemiological data sets.

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
