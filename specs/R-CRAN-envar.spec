%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  envar
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Process Environmental Variables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-usdm 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-rangeBuilder 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-usdm 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fs 
Requires:         R-utils 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-rangeBuilder 

%description
Provides a unified interface to download, harmonise and extract a wide
range of environmental and socio-economic variables from established open
data web services (such as 'WorldClim' <https://www.worldclim.org/>,
'CHELSA' <https://chelsa-climate.org/> and 'Bio-ORACLE'
<https://www.bio-oracle.org/>, among others) for use in macroecology and
biogeography. The package handles spatial subsetting to a study area,
reprojection to a common coordinate reference system, and extraction of
values at sampling points, so that predictors from heterogeneous sources
can be assembled within a single reproducible workflow. Helper functions
for collinearity checking and variable exploration are also included.

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
