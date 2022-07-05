%global __brp_check_rpaths %{nil}
%global packname  SensMap
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Sensory and Consumer Data Mapping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-glmulti 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-glmulti 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
Provides Sensory and Consumer Data mapping and analysis
<doi:10.14569/IJACSA.2017.081266>. The mapping visualization is made
available from several features : options in dimension reduction methods
and prediction models ranging from linear to non linear regressions. A
smoothed version of the map performed using locally weighted regression
algorithm is available. A selection process of map stability is provided.
A 'shiny' application is included. It presents an easy GUI for the
implemented functions as well as a comparative tool of fit models using
several criteria. Basic analysis such as characterization of products,
panelists and sessions likewise consumer segmentation are also made
available.

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
