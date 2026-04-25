%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pep725
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pan-European Phenological Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mgcv 
Requires:         R-methods 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-sf 

%description
Provides a framework for quality-aware analysis of ground-based
phenological data from the PEP725 Pan-European Phenology Database (Templ
et al. (2018) <doi:10.1007/s00484-018-1512-8>; Templ et al. (2026)
<doi:10.1111/nph.70869>) and similar observation networks. Implements
station-level data quality grading, outlier detection, phenological
normals (climate baselines), anomaly detection, elevation and latitude
gradient estimation with robust regression, spatial synchrony
quantification, partial least squares (PLS) regression for identifying
temperature-sensitive periods, and sequential Mann-Kendall trend analysis.
Supports data import from PEP725 files, conversion of user-supplied data,
and downloadable synthetic datasets for teaching without barriers of
registration. All analysis outputs provide 'print', 'summary', and 'plot'
methods. Interactive spatial visualization is available via 'leaflet'.

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
