%global __brp_check_rpaths %{nil}
%global packname  photobiology
%global packver   0.10.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.8
Release:          1%{?dist}%{?buildtag}
Summary:          Photobiological Calculations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.4
BuildRequires:    R-CRAN-zoo >= 1.8.8
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-lubridate >= 1.7.8
BuildRequires:    R-CRAN-polynom >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-splus2R >= 1.2.2
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-rlang >= 0.4.8
BuildRequires:    R-stats 
Requires:         R-CRAN-tibble >= 3.0.4
Requires:         R-CRAN-zoo >= 1.8.8
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-lubridate >= 1.7.8
Requires:         R-CRAN-polynom >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-splus2R >= 1.2.2
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-rlang >= 0.4.8
Requires:         R-stats 

%description
Definitions of classes, methods, operators and functions for use in
photobiology and radiation meteorology and climatology. Calculation of
effective (weighted) and not-weighted irradiances/doses, fluence rates,
transmittance, reflectance, absorptance, absorbance and diverse ratios and
other derived quantities from spectral data. Local maxima and minima:
peaks, valleys and spikes. Conversion between energy-and photon-based
units. Wavelength interpolation. Astronomical calculations related solar
angles and day length. Colours and vision. This package is part of the
'r4photobiology' suite, Aphalo, P. J. (2015)
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
