%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  connections
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Integrates with the 'RStudio' Connections Pane and 'pins'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pins 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-rscontract 
Requires:         R-CRAN-DBI 
Requires:         R-methods 
Requires:         R-CRAN-pins 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-rscontract 

%description
Enables 'DBI' compliant packages to integrate with the 'RStudio'
connections pane, and the 'pins' package. It automates the display of
schemata, tables, views, as well as the preview of the table's top 1000
records.

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
