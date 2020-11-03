%global packname  datacleanr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive and Reproducible Data Cleaning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-summarytools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-shinyFiles 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-summarytools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-utils 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-tools 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-shinyFiles 

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
