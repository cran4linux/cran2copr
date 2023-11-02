%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  doBy
%global packver   4.6.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.6.20
Release:          1%{?dist}%{?buildtag}
Summary:          Groupwise Statistics, LSmeans, Linear Estimates, Utilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pbkrtest >= 0.4.8.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-pbkrtest >= 0.4.8.1
Requires:         R-methods 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-tibble 

%description
Utility package containing: 1) Facilities for working with grouped data:
'do' something to data stratified 'by' some variables. 2) LSmeans
(least-squares means), general linear estimates. 3) Restrict functions to
a smaller domain. 4) Miscellaneous other utilities.

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
