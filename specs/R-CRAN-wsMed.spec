%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wsMed
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Within-Subject Mediation Analysis Using Structural Equation Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-semmcci 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-semboottools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-semmcci 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-semboottools 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-stats 

%description
Within-subject mediation analysis using structural equation modeling.
Examine how changes in an outcome variable between two conditions are
mediated through one or more variables. Supports within-subject mediation
analysis using the 'lavaan' package by Rosseel (2012)
<doi:10.18637/jss.v048.i02>, and extends Monte Carlo confidence interval
estimation to missing data scenarios using the 'semmcci' package by
Pesigan and Cheung (2023) <doi:10.3758/s13428-023-02114-4>.

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
