%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinymrp
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface for Multilevel Regression and Poststratification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.8.0
BuildRequires:    R-CRAN-golem >= 0.4.1
BuildRequires:    R-CRAN-config >= 0.3.2
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-qs2 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-waiter 
Requires:         R-CRAN-shiny >= 1.8.0
Requires:         R-CRAN-golem >= 0.4.1
Requires:         R-CRAN-config >= 0.3.2
Requires:         R-CRAN-bsicons 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-highcharter 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-qs2 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-waiter 

%description
Dual interfaces, graphical and programmatic, designed for intuitive
applications of Multilevel Regression and Poststratification (MRP). Users
can apply the method to a variety of datasets, from electronic health
records to sample survey data, through an end-to-end Bayesian data
analysis workflow. The package provides robust tools for data cleaning,
exploratory analysis, flexible model building, and insightful result
visualization. For more details, see Si et al. (2020)
<https://www150.statcan.gc.ca/n1/en/pub/12-001-x/2020002/article/00003-eng.pdf?st=iF1_Fbrh>
and Si (2025) <doi:10.1214/24-STS932>.

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
