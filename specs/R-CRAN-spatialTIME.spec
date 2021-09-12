%global __brp_check_rpaths %{nil}
%global packname  spatialTIME
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Analysis of Vectra Immunoflourescent Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.core 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-grDevices 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.core 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-viridis 

%description
Visualization and analysis of Vectra Immunoflourescent data. Options for
calculating both the univariate and bivariate Ripley's K are included.
Calculations are performed using a permutation-based approach presented by
Wilson et al.  <doi:10.1101/2021.04.27.21256104>.

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
