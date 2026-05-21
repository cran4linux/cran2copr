%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geobr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Official Spatial Data Sets of Brazil

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.0.0
BuildRequires:    R-CRAN-duckspatial >= 1.1.0
BuildRequires:    R-CRAN-sf >= 0.9.3
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nanoarrow 
BuildRequires:    R-CRAN-piggyback 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 5.0.0
Requires:         R-CRAN-duckspatial >= 1.1.0
Requires:         R-CRAN-sf >= 0.9.3
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-httr2 
Requires:         R-methods 
Requires:         R-CRAN-nanoarrow 
Requires:         R-CRAN-piggyback 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Easy access to official spatial data sets of Brazil. The package offers a
wide range of spatial data sets available at various geographic scales and
for various years with harmonized attributes, projection and fixed
topology. All functions allow for seamless integration sf, DuckDB and
Arrow.

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
