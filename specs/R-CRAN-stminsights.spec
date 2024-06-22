%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stminsights
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          A 'Shiny' Application for Inspecting Structural Topic Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-ggraph >= 2.2.1
BuildRequires:    R-CRAN-readr >= 2.1.5
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-igraph >= 2.0.3
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-stm >= 1.3.7
BuildRequires:    R-CRAN-huge >= 1.3.5
BuildRequires:    R-CRAN-tidygraph >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-ggrepel >= 0.9.5
BuildRequires:    R-CRAN-shinydashboard >= 0.7.2
BuildRequires:    R-CRAN-shinyBS >= 0.6.0
BuildRequires:    R-CRAN-DT >= 0.33
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-ggraph >= 2.2.1
Requires:         R-CRAN-readr >= 2.1.5
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-igraph >= 2.0.3
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-stm >= 1.3.7
Requires:         R-CRAN-huge >= 1.3.5
Requires:         R-CRAN-tidygraph >= 1.3.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-ggrepel >= 0.9.5
Requires:         R-CRAN-shinydashboard >= 0.7.2
Requires:         R-CRAN-shinyBS >= 0.6.0
Requires:         R-CRAN-DT >= 0.33
Requires:         R-stats 
Requires:         R-CRAN-scales 

%description
This app enables interactive validation, interpretation and visualization
of structural topic models from the 'stm' package by Roberts and others
(2014) <doi:10.1111/ajps.12103>. It also includes helper functions for
model diagnostics and extracting data from effect estimates.

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
