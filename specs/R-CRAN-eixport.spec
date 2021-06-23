%global __brp_check_rpaths %{nil}
%global packname  eixport
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Export Emissions to Atmospheric Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cptcity 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-cptcity 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-data.table 

%description
Emissions are the mass of pollutants released into the atmosphere. Air
quality models need emissions data, with spatial and temporal
distribution, to represent air pollutant concentrations. This package,
eixport, creates inputs for the air quality models 'WRF-Chem' Grell et al
(2005) <doi:10.1016/j.atmosenv.2005.04.027>, 'MUNICH' Kim et al (2018)
<doi:10.5194/gmd-11-611-2018> , 'BRAMS-SPM' Freitas et al (2005)
<doi:10.1016/j.atmosenv.2005.07.017> and 'RLINE' Snyder et al (2013)
<doi:10.1016/j.atmosenv.2013.05.074>. See the 'eixport' website
(<https://atmoschem.github.io/eixport/>) for more information,
documentations and examples. More details in Ibarra-Espinosa et al (2018)
<doi:10.21105/joss.00607>.

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
