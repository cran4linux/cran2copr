%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eHDPrep
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Quality Control and Semantic Enrichment of Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-tibble >= 3.0.5
BuildRequires:    R-CRAN-quanteda >= 2.1.2
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.31
BuildRequires:    R-CRAN-kableExtra >= 1.3.1
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-igraph >= 1.2.6
BuildRequires:    R-CRAN-tidygraph >= 1.2.0
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-pheatmap >= 1.0.12
BuildRequires:    R-CRAN-tm >= 0.7.8
BuildRequires:    R-CRAN-forcats >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-tibble >= 3.0.5
Requires:         R-CRAN-quanteda >= 2.1.2
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-knitr >= 1.31
Requires:         R-CRAN-kableExtra >= 1.3.1
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-igraph >= 1.2.6
Requires:         R-CRAN-tidygraph >= 1.2.0
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-pheatmap >= 1.0.12
Requires:         R-CRAN-tm >= 0.7.8
Requires:         R-CRAN-forcats >= 0.5.0
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-purrr >= 0.3.4

%description
A tool for the preparation and enrichment of health datasets for analysis
(Toner et al. (2023) <doi:10.1093/gigascience/giad030>). Provides
functionality for assessing data quality and for improving the reliability
and machine interpretability of a dataset. 'eHDPrep' also enables semantic
enrichment of a dataset where metavariables are discovered from the
relationships between input variables determined from user-provided
ontologies.

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
