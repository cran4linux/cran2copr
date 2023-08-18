%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shiny.emptystate
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Empty State Components for 'Shiny'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fontawesome 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
Requires:         R-CRAN-fontawesome 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-shiny 
Requires:         R-utils 

%description
Offers a comprehensive solution for managing 'empty states' in 'Shiny'
applications. It provides tools to create both default and customizable
components for scenarios where data is absent or doesn't match
user-defined filters. The package prioritizes user experience, ensuring
clarity and consistency even when data is not available to display.

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
