%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RawHummus
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Raw Data Quality Control Tool for LC-MS System

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-golem >= 0.3.5.9001
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RaMS 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shinycustomloader 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-shinyMatrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-golem >= 0.3.5.9001
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RaMS 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shinycustomloader 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-shinyMatrix 
Requires:         R-stats 
Requires:         R-utils 

%description
Assess LC–MS system performance by visualizing instrument log files and
monitoring raw quality control samples within a project.

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
