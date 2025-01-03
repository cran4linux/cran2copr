%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TestAnaAPP
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A 'shiny' App for Test Analysis and Visualization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-difR >= 5.1
BuildRequires:    R-CRAN-openxlsx >= 4.2.5.2
BuildRequires:    R-CRAN-plotrix >= 3.8.2
BuildRequires:    R-CRAN-ggplot2 >= 3.4.3
BuildRequires:    R-CRAN-bruceR >= 2023.8
BuildRequires:    R-CRAN-rmarkdown >= 2.24
BuildRequires:    R-CRAN-shiny >= 1.7.5
BuildRequires:    R-CRAN-EstCRM >= 1.6
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-mirt >= 1.42
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-semPlot >= 1.1.6
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-cowplot >= 1.1.1
BuildRequires:    R-CRAN-shinycssloaders >= 1.0.0
BuildRequires:    R-CRAN-flextable >= 0.9.2
BuildRequires:    R-CRAN-shinydashboard >= 0.7.2
BuildRequires:    R-CRAN-latticeExtra >= 0.6.30
BuildRequires:    R-CRAN-officer >= 0.6.2
BuildRequires:    R-CRAN-golem >= 0.4.1
BuildRequires:    R-CRAN-lordif >= 0.3.3
BuildRequires:    R-CRAN-officedown >= 0.3.0
BuildRequires:    R-CRAN-DT >= 0.29
Requires:         R-CRAN-difR >= 5.1
Requires:         R-CRAN-openxlsx >= 4.2.5.2
Requires:         R-CRAN-plotrix >= 3.8.2
Requires:         R-CRAN-ggplot2 >= 3.4.3
Requires:         R-CRAN-bruceR >= 2023.8
Requires:         R-CRAN-rmarkdown >= 2.24
Requires:         R-CRAN-shiny >= 1.7.5
Requires:         R-CRAN-EstCRM >= 1.6
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-mirt >= 1.42
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-semPlot >= 1.1.6
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-cowplot >= 1.1.1
Requires:         R-CRAN-shinycssloaders >= 1.0.0
Requires:         R-CRAN-flextable >= 0.9.2
Requires:         R-CRAN-shinydashboard >= 0.7.2
Requires:         R-CRAN-latticeExtra >= 0.6.30
Requires:         R-CRAN-officer >= 0.6.2
Requires:         R-CRAN-golem >= 0.4.1
Requires:         R-CRAN-lordif >= 0.3.3
Requires:         R-CRAN-officedown >= 0.3.0
Requires:         R-CRAN-DT >= 0.29

%description
This application provides exploratory and confirmatory factor analysis,
classical test theory, unidimensional and multidimensional item response
theory, and continuous item response model analysis, through the 'shiny'
interactive interface. In addition, it offers rich functionalities for
visualizing and downloading results. Users can download figures, tables,
and analysis reports via the interactive interface.

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
