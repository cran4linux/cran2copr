%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  teal.picks
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dataset and Variable Picker and Merge Module for 'teal' Applications

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-teal 
BuildRequires:    R-CRAN-teal.code 
BuildRequires:    R-CRAN-teal.data 
BuildRequires:    R-CRAN-teal.logger 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-bsicons 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-logger 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-teal 
Requires:         R-CRAN-teal.code 
Requires:         R-CRAN-teal.data 
Requires:         R-CRAN-teal.logger 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-yaml 

%description
Allows users to interactively select datasets, variables, and values
within 'teal' applications using a 'tidyselect'-style interface. Selected
picks can be merged and transformed into analysis-ready data within 'teal'
modules.

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
