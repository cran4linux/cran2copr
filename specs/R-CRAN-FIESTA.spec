%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FIESTA
%global packver   3.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Inventory Estimation and Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FIESTAutils >= 1.3.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-gdalraster 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-utils 
Requires:         R-CRAN-FIESTAutils >= 1.3.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-gdalraster 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sqldf 
Requires:         R-utils 

%description
A research estimation tool for analysts that work with sample-based
inventory data from the U.S. Department of Agriculture, Forest Service,
Forest Inventory and Analysis (FIA) Program.

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
