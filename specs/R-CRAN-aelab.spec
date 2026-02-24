%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aelab
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Processing for Aquatic Ecology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-FSA 
BuildRequires:    R-CRAN-rcompanion 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggspatial 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lubridate 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-grDevices 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-FSA 
Requires:         R-CRAN-rcompanion 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggspatial 

%description
Facilitate the analysis of data related to aquatic ecology, specifically
the establishment of carbon budget. Currently, the package allows the
below analysis. (i) the calculation of greenhouse gas flux based on data
obtained from trace gas analyzer using the method described in Lin et al.
(2024). (ii) the calculation of Dissolved Oxygen (DO) metabolism based on
data obtained from dissolved oxygen data logger using the method described
in Staehr et al. (2010). Yong et al. (2024) <doi:10.5194/bg-21-5247-2024>.
Staehr et al. (2010) <doi:10.4319/lom.2010.8.0628>.

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
