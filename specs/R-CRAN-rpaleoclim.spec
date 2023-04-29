%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rpaleoclim
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Paleoclimate Data from 'PaleoClim'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
'PaleoClim' <http://www.paleoclim.org> (Brown et al. 2019,
<doi:10.1038/sdata.2018.254>) is a set of free, high resolution
paleoclimate surfaces covering the whole globe. It includes data on
surface temperature, precipitation and the standard bioclimatic variables
commonly used in ecological modelling, derived from the 'HadCM3' general
circulation model and downscaled to a spatial resolution of up to 2.5
minutes. Simulations are available for key time periods from the Late
Holocene to mid-Pliocene. Data on current and Last Glacial Maximum climate
is derived from 'CHELSA' (Karger et al. 2017,
<doi:10.1038/sdata.2017.122>) and reprocessed by 'PaleoClim' to match
their format; it is available at up to 30 seconds resolution. This package
provides a simple interface for downloading 'PaleoClim' data in R, with
support for caching and filtering retrieved data by period, resolution,
and geographic extent.

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
