%global packname  rFIA
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Space-Time Estimation of Forest Variables using the FIA Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-dtplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-dtplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sf 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 

%description
The goal of 'rFIA' is to increase the accessibility and use of the United
States Forest Services (USFS) Forest Inventory and Analysis (FIA) Database
by providing a user-friendly, open source toolkit to easily query and
analyze FIA Data. Designed to accommodate a wide range of potential user
objectives, 'rFIA' simplifies the estimation of forest variables from the
FIA Database and allows all R users (experts and newcomers alike) to
unlock the flexibility inherent to the Enhanced FIA design. Specifically,
'rFIA' improves accessibility to the spatio-temporal estimation capacity
of the FIA Database by producing space-time indexed summaries of forest
variables within user-defined population boundaries. Direct integration
with other popular R packages (e.g., 'dplyr', 'tidyr', and 'sf')
facilitates efficient space-time query and data summary, and supports
common data representations and API design. The package implements
design-based estimation procedures outlined by Bechtold & Patterson (2005)
<doi:10.2737/SRS-GTR-80>, and has been validated against estimates and
sampling errors produced by FIA 'EVALIDator'. Current development is
focused on the implementation of spatially-enabled model-assisted
estimators to improve population, change, and ratio estimates.

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
