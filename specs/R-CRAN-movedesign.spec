%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  movedesign
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Study Design Toolbox for Movement Ecology Studies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-ctmm >= 0.6.1
BuildRequires:    R-CRAN-golem >= 0.3.2
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-bsplus 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fontawesome 
BuildRequires:    R-CRAN-gdtools 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-shinyFeedback 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-ctmm >= 0.6.1
Requires:         R-CRAN-golem >= 0.3.2
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-bsplus 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fontawesome 
Requires:         R-CRAN-gdtools 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggtext 
Requires:         R-grDevices 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-lubridate 
Requires:         R-parallel 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-quarto 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-shinyFeedback 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-viridis 

%description
Toolbox and 'shiny' application to help researchers design movement
ecology studies, focusing on two key objectives: estimating home range
areas, and estimating fine-scale movement behavior, specifically speed and
distance traveled. It provides interactive simulations and methodological
guidance to support study planning and decision-making. The application is
described in Silva et al. (2023) <doi:10.1111/2041-210X.14153>.

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
