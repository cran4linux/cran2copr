%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  onmaRg
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Import Public Health Ontario's Ontario Marginalization Index

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
The Ontario Marginalization Index is a socioeconomic model that is built
on Statistics Canada census data. The model consists of four dimensions:
Residential Instability, Material Deprivation, Dependency and Ethnic
Concentration. Each of these dimensions are imported for a variety of
geographic levels (DA, CD, etc.) for both the 2011 and 2016
administrations of the census (2021 pending). These data sets contribute
to community analysis of equity with respect to Ontario's Anti-Racism Act.
The Ontario Marginalization Index data is retrieved from the Public Health
Ontario website:
<https://www.publichealthontario.ca/en/data-and-analysis/health-equity/ontario-marginalization-index>.
The shapefile data is retrieved from the Statistics Canada website:
<https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-eng.cfm>.

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
