%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tRigon
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Toolbox for Integrative Pathomics Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.94
BuildRequires:    R-CRAN-randomForest >= 4.7.1.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-shinydashboardPlus >= 2.0.3
BuildRequires:    R-CRAN-shiny >= 1.7.4.1
BuildRequires:    R-CRAN-markdown >= 1.7
BuildRequires:    R-CRAN-readxl >= 1.4.3
BuildRequires:    R-CRAN-writexl >= 1.4.2
BuildRequires:    R-CRAN-boot >= 1.3.28
BuildRequires:    R-CRAN-sessioninfo >= 1.2.2
BuildRequires:    R-CRAN-data.table >= 1.14.8
BuildRequires:    R-CRAN-simpleboot >= 1.1.7
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-patchwork >= 1.1.2
BuildRequires:    R-CRAN-factoextra >= 1.0.7
BuildRequires:    R-CRAN-shinyWidgets >= 0.7.6
BuildRequires:    R-CRAN-shinydashboard >= 0.7.2
BuildRequires:    R-CRAN-ggpubr >= 0.6.0
BuildRequires:    R-CRAN-ggridges >= 0.5.4
BuildRequires:    R-CRAN-DT >= 0.28
BuildRequires:    R-CRAN-ggcorrplot >= 0.1.4
Requires:         R-CRAN-caret >= 6.0.94
Requires:         R-CRAN-randomForest >= 4.7.1.1
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-shinydashboardPlus >= 2.0.3
Requires:         R-CRAN-shiny >= 1.7.4.1
Requires:         R-CRAN-markdown >= 1.7
Requires:         R-CRAN-readxl >= 1.4.3
Requires:         R-CRAN-writexl >= 1.4.2
Requires:         R-CRAN-boot >= 1.3.28
Requires:         R-CRAN-sessioninfo >= 1.2.2
Requires:         R-CRAN-data.table >= 1.14.8
Requires:         R-CRAN-simpleboot >= 1.1.7
Requires:         R-CRAN-RColorBrewer >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-patchwork >= 1.1.2
Requires:         R-CRAN-factoextra >= 1.0.7
Requires:         R-CRAN-shinyWidgets >= 0.7.6
Requires:         R-CRAN-shinydashboard >= 0.7.2
Requires:         R-CRAN-ggpubr >= 0.6.0
Requires:         R-CRAN-ggridges >= 0.5.4
Requires:         R-CRAN-DT >= 0.28
Requires:         R-CRAN-ggcorrplot >= 0.1.4

%description
Processing and analysis of pathomics, omics and other medical datasets.
'tRigon' serves as a toolbox for descriptive and statistical analysis,
correlations, plotting and many other methods for exploratory analysis of
high-dimensional datasets.

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
