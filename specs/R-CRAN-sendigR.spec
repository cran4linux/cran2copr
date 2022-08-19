%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sendigR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Enable Cross-Study Analysis of 'CDISC' 'SEND' Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-cicerone 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-sjlabelled 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-cicerone 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-sjlabelled 

%description
A system enables cross study Analysis by extracting and filtering study
data for control animals from 'CDISC' 'SEND' Study Repository. These data
types are supported: Body Weights, Laboratory test results and Microscopic
findings. These database types are supported: 'SQLite' and 'Oracle'.

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
