%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iRfcb
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Managing Imaging FlowCytobot (IFCB) Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 6.0.0
BuildRequires:    R-CRAN-reticulate >= 1.41.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-worrms 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-curl >= 6.0.0
Requires:         R-CRAN-reticulate >= 1.41.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-png 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-worrms 
Requires:         R-CRAN-zip 

%description
A comprehensive suite of tools for managing, processing, and analyzing
data from the IFCB. I R FlowCytobot ('iRfcb') supports quality control,
geospatial analysis, and preparation of IFCB data for publication in
databases like <https://www.gbif.org>, <https://www.obis.org>,
<https://emodnet.ec.europa.eu/en>, <https://shark.smhi.se/>, and
<https://www.ecotaxa.org>. The package integrates with the MATLAB
'ifcb-analysis' tool, which is described in Sosik and Olson (2007)
<doi:10.4319/lom.2007.5.204>, and provides features for working with raw,
manually classified, and machine learning–classified image datasets. Key
functionalities include image extraction, particle size distribution
analysis, taxonomic data handling, and biomass concentration calculations,
essential for plankton research.

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
