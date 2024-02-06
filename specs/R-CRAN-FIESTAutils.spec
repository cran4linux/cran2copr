%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FIESTAutils
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Utility Functions for Forest Inventory Estimation and Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-gdalraster 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-hbsae 
BuildRequires:    R-CRAN-JoSAE 
BuildRequires:    R-CRAN-mase 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-sae 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-gdalraster 
Requires:         R-graphics 
Requires:         R-CRAN-hbsae 
Requires:         R-CRAN-JoSAE 
Requires:         R-CRAN-mase 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-sae 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sqldf 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-units 
Requires:         R-utils 

%description
A set of tools for data wrangling, spatial data analysis, statistical
modeling (including direct, model-assisted, photo-based, and small area
tools), and USDA Forest Service data base tools. These tools are aimed to
help Foresters, Analysts, and Scientists extract and perform analyses on
USDA Forest Service data.

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
