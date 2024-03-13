%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epwshiftr
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Create Future 'EnergyPlus' Weather Files using 'CMIP6' Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-eplusr >= 0.15.2
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-PCICt 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-psychrolib 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-RNetCDF 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-eplusr >= 0.15.2
Requires:         R-CRAN-fst 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-PCICt 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-psychrolib 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-RNetCDF 
Requires:         R-CRAN-units 

%description
Query, download climate change projection data from the 'CMIP6' (Coupled
Model Intercomparison Project Phase 6) project
<https://pcmdi.llnl.gov/CMIP6/> in the 'ESGF' (Earth System Grid
Federation) platform <https://esgf.llnl.gov>, and create future
'EnergyPlus' <https://energyplus.net> Weather ('EPW') files adjusted from
climate changes using data from Global Climate Models ('GCM').

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
