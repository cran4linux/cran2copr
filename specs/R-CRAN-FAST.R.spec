%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FAST.R
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze and Visualize FAST-Generated Data

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plater 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyFeedback 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-waiter 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plater 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyFeedback 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-waiter 
Requires:         R-CRAN-zip 

%description
R 'shiny' app to perform data analysis and visualization for the Fully
Automated Senescence Test (FAST) workflow.

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
