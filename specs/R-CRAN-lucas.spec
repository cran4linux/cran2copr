%global __brp_check_rpaths %{nil}
%global packname  lucas
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Package to Download and Create the DB of LUCAS Data Harmonized

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-rpostgis 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-DBI 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-rpostgis 
Requires:         R-CRAN-plyr 
Requires:         R-utils 
Requires:         R-CRAN-DBI 

%description
Reproduces the harmonized DB of the ESTAT survey of the same name. The
survey data is served as separate spreadsheets with noticeable differences
in the collected attributes. The tool here presented carries out a series
of instructions that harmonize the attributes in terms of name, meaning,
and occurrence, while also introducing a series of new variables,
instrumental to adding value to the product. Outputs include one
harmonized table with all the years, and three separate geometries,
corresponding to the theoretical point, the gps location where the
measurement was made and the 250m east-facing transect.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
