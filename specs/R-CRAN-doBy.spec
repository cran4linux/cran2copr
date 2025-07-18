%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  doBy
%global packver   4.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Groupwise Statistics, LSmeans, Linear Estimates, Utilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-modelr 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-modelr 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Utility package containing: Main categories: Working with grouped data:
'do' something to data when stratified 'by' some variables.  General
linear estimates. Data handling utilities. Functional programming, in
particular restrict functions to a smaller domain. Miscellaneous functions
for data handling. Model stability in connection with model selection.
Miscellaneous other tools.

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
