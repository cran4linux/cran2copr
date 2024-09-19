%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QBMS
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Query the Breeding Management System(s)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-tcltk 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RNetCDF 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-tcltk 
Requires:         R-utils 
Requires:         R-CRAN-RNetCDF 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 

%description
This R package assists breeders in linking data systems with their
analytic pipelines, a crucial step in digitizing breeding processes. It
supports querying and retrieving phenotypic and genotypic data from
systems like 'EBS' <https://ebs.excellenceinbreeding.org/>, 'BMS'
<https://bmspro.io>, 'BreedBase' <https://breedbase.org>, and 'GIGWA'
<https://github.com/SouthGreenPlatform/Gigwa2> (using 'BrAPI'
<https://brapi.org> calls). Extra helper functions support environmental
data sources, including 'TerraClimate'
<https://www.climatologylab.org/terraclimate.html> and 'FAO' 'HWSDv2'
<https://gaez.fao.org/pages/hwsd> soil database.

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
