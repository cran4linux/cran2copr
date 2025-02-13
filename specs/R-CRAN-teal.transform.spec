%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  teal.transform
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Extracting and Merging Data in the 'teal' Framework

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-teal.data >= 0.7.0
BuildRequires:    R-CRAN-teal.widgets >= 0.4.3
BuildRequires:    R-CRAN-teal.logger >= 0.3.1
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-logger >= 0.2.0
BuildRequires:    R-CRAN-shinyvalidate >= 0.1.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-teal.data >= 0.7.0
Requires:         R-CRAN-teal.widgets >= 0.4.3
Requires:         R-CRAN-teal.logger >= 0.3.1
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-logger >= 0.2.0
Requires:         R-CRAN-shinyvalidate >= 0.1.3
Requires:         R-methods 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
A standardized user interface for column selection, that facilitates
dataset merging in 'teal' framework.

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
