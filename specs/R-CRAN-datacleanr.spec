%global __brp_check_rpaths %{nil}
%global packname  datacleanr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive and Reproducible Data Cleaning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.2.1
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-lubridate >= 1.7.9.2
BuildRequires:    R-CRAN-formatR >= 1.7
BuildRequires:    R-CRAN-htmlwidgets >= 1.5.3
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-fs >= 1.5.0
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-summarytools >= 0.9.6
BuildRequires:    R-CRAN-shinyFiles >= 0.8.0
BuildRequires:    R-CRAN-clipr >= 0.7.1
BuildRequires:    R-CRAN-shinyWidgets >= 0.5.4
BuildRequires:    R-CRAN-htmltools >= 0.5
BuildRequires:    R-CRAN-rlang >= 0.4.9
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-DT >= 0.16
BuildRequires:    R-CRAN-rstudioapi >= 0.13
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-bslib 
Requires:         R-CRAN-plotly >= 4.9.2.1
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-lubridate >= 1.7.9.2
Requires:         R-CRAN-formatR >= 1.7
Requires:         R-CRAN-htmlwidgets >= 1.5.3
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-fs >= 1.5.0
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-summarytools >= 0.9.6
Requires:         R-CRAN-shinyFiles >= 0.8.0
Requires:         R-CRAN-clipr >= 0.7.1
Requires:         R-CRAN-shinyWidgets >= 0.5.4
Requires:         R-CRAN-htmltools >= 0.5
Requires:         R-CRAN-rlang >= 0.4.9
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-DT >= 0.16
Requires:         R-CRAN-rstudioapi >= 0.13
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-bslib 

%description
Flexible and efficient cleaning of data with interactivity. 'datacleanr'
facilitates best practices in data analyses and reproducibility with
built-in features and by translating interactive/manual operations to
code. The package is designed for interoperability, and so seamlessly fits
into reproducible analyses pipelines in 'R'.

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
