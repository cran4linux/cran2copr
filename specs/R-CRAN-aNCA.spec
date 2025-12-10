%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aNCA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          (Pre-)Clinical NCA in a Dynamic Shiny App

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-PKNCA >= 0.12.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-formatters 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rlistings 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tern 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-utils 
Requires:         R-CRAN-PKNCA >= 0.12.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-formatters 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rlistings 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tern 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-units 
Requires:         R-utils 

%description
An interactive 'shiny' application for performing non-compartmental
analysis (NCA) on pre-clinical and clinical pharmacokinetic data. The
package builds on 'PKNCA' for core estimators and provides interactive
visualizations, CDISC outputs ('ADNCA', 'PP', 'ADPP') and configurable
TLGs (tables, listings, and graphs). Typical use cases include exploratory
analysis, validation, reporting or teaching/demonstration of NCA methods.
Methods and core estimators are described in Denney, Duvvuri, and
Buckeridge (2015) "Simple, Automatic Noncompartmental Analysis: The PKNCA
R Package" <doi:10.1007/s10928-015-9432-2>.

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
