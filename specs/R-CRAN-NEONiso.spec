%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NEONiso
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Calibrate and Work with NEON Atmospheric Isotope Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-neonUtilities >= 2.3.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-neonUtilities >= 2.3.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Functions for downloading, calibrating, and analyzing atmospheric isotope
data bundled into the eddy covariance data products of the National
Ecological Observatory Network (NEON) <https://www.neonscience.org>.
Calibration tools are provided for carbon and water isotope products.
Carbon isotope calibration details are found in Fiorella et al. (2021)
<doi:10.1029/2020JG005862>, and the readme file at
<https://github.com/lanl/NEONiso>. Tools for calibrating water isotope
products have been added as of 0.6.0, but have known deficiencies and
should be considered experimental and unsupported.

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
