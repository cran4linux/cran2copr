%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GRShiny
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graded Response Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-sass 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-sirt 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-MASS 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-sass 

%description
Simulation and analysis of graded response data with different types of
estimators. Also, an interactive shiny application is provided with
graphics for characteristic and information curves. Samejima (2018)
<doi:10.1007/978-1-4757-2691-6_5>.

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
