%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyCohortBuilder
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Modular Cohort-Building Framework for Analytical Dashboards

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-rlang >= 1.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.7.0
BuildRequires:    R-CRAN-shinyGizmo >= 0.4.2
BuildRequires:    R-CRAN-cohortBuilder >= 0.3.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tryCatchLog 
BuildRequires:    R-CRAN-highr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-rlang >= 1.0
Requires:         R-CRAN-shinyWidgets >= 0.7.0
Requires:         R-CRAN-shinyGizmo >= 0.4.2
Requires:         R-CRAN-cohortBuilder >= 0.3.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tryCatchLog 
Requires:         R-CRAN-highr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lifecycle 

%description
You can easily add advanced cohort-building component to your analytical
dashboard or simple 'Shiny' app. Then you can instantly start building
cohorts using multiple filters of different types, filtering datasets, and
filtering steps. Filters can be complex and data-specific, and together
with multiple filtering steps you can use complex filtering rules. The
cohort-building sidebar panel allows you to easily work with filters, add
and remove filtering steps. It helps you with handling missing values
during filtering, and provides instant filtering feedback with filter
feedback plots. The GUI panel is not only compatible with native shiny
bookmarking, but also provides reproducible R code.

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
