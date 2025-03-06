%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PhenoSpectra
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multispectral Data Analysis and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-stats 

%description
Provides tools for processing, analyzing, and visualizing spectral data
collected from 3D laser-based scanning systems. Supports applications in
agriculture, forestry, environmental monitoring, industrial quality
control, and biomedical research. Enables evaluation of plant growth,
productivity, resource efficiency, disease management, and pest
monitoring. Includes statistical methods for extracting insights from
multispectral and hyperspectral data and generating publication-ready
visualizations. See Zieschank & Junker (2023)
<doi:10.3389/fpls.2023.1141554> and Saric et al. (2022)
<doi:10.1016/J.TPLANTS.2021.12.003> for related work.

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
