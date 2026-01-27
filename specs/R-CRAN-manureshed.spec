%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  manureshed
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatiotemporal Nutrient Balance Analysis Across Agricultural and Municipal Systems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-tigris >= 1.5.0
BuildRequires:    R-CRAN-igraph >= 1.2.0
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-tigris >= 1.5.0
Requires:         R-CRAN-igraph >= 1.2.0
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 

%description
A comprehensive framework for analyzing agricultural nutrient balances
across multiple spatial scales (county, 'HUC8', 'HUC2') with integration
of wastewater treatment plant ('WWTP') effluent loads for both nitrogen
and phosphorus. Supports classification of spatial units as nutrient
sources, sinks, or balanced areas based on agricultural surplus and
deficit calculations. Includes visualization tools, spatial transition
probability analysis, and nutrient flow network mapping. Built-in datasets
include agricultural nutrient balance data from the Nutrient Use
Geographic Information System ('NuGIS'; The Fertilizer Institute and Plant
Nutrition Canada, 1987-2016) <https://nugis.tfi.org/tabular_data/> and
U.S. Environmental Protection Agency ('EPA') wastewater discharge data
from the 'ECHO' Discharge Monitoring Report ('DMR') Loading Tool
(2007-2016)
<https://echo.epa.gov/trends/loading-tool/water-pollution-search>. Data
are downloaded on demand from the Open Science Framework ('OSF')
repository to minimize package size while maintaining full functionality.
The integrated 'manureshed' framework methodology is described in Akanbi
et al. (2025) <doi:10.1016/j.resconrec.2025.108697>. Designed for nutrient
management planning, environmental analysis, and circular economy research
at watershed/administrative to national scales. This material is based
upon financial support by the National Science Foundation, EEC Division of
Engineering Education and Centers, NSF Engineering Research Center for
Advancing Sustainable and Distributed Fertilizer Production (CASFER), NSF
20-553 Gen-4 Engineering Research Centers award 2133576. We thank Dr.
Robert D. Sabo (U.S. Environmental Protection Agency) for his valuable
contributions to the conceptual development and review of this work.

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
