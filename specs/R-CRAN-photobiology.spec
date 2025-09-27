%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  photobiology
%global packver   0.14.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.0
Release:          1%{?dist}%{?buildtag}
Summary:          Photobiological Calculations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-lubridate >= 1.9.4
BuildRequires:    R-CRAN-plyr >= 1.8.9
BuildRequires:    R-CRAN-zoo >= 1.8.12
BuildRequires:    R-CRAN-polynom >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-splus2R >= 1.3.3
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-caTools >= 1.18.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-SunCalcMeeus >= 0.1.3
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-lubridate >= 1.9.4
Requires:         R-CRAN-plyr >= 1.8.9
Requires:         R-CRAN-zoo >= 1.8.12
Requires:         R-CRAN-polynom >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-splus2R >= 1.3.3
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-caTools >= 1.18.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-SunCalcMeeus >= 0.1.3
Requires:         R-stats 
Requires:         R-grDevices 

%description
Definitions of classes, methods, operators and functions for use in
photobiology and radiation meteorology and climatology. Calculation of
effective (weighted) and not-weighted irradiances/doses, fluence rates,
transmittance, reflectance, absorptance, absorbance and diverse ratios and
other derived quantities from spectral data. Local maxima and minima:
peaks, valleys and spikes. Conversion between energy-and photon-based
units. Wavelength interpolation. Colours and vision. This package is part
of the 'r4photobiology' suite, Aphalo, P. J. (2015)
<doi:10.19232/uv4pb.2015.1.14>.

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
