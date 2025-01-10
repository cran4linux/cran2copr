%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3shiny
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning in 'shiny' with 'mlr3'

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-shinyjs >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-mlr3measures >= 0.3.1
BuildRequires:    R-CRAN-mlr3 >= 0.12.0
BuildRequires:    R-CRAN-DT >= 0.11
BuildRequires:    R-CRAN-mlr3learners 
BuildRequires:    R-CRAN-mlr3pipelines 
BuildRequires:    R-CRAN-mlr3viz 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-ggparty 
BuildRequires:    R-CRAN-GGally 
Requires:         R-CRAN-shinyjs >= 2.0.0
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-mlr3measures >= 0.3.1
Requires:         R-CRAN-mlr3 >= 0.12.0
Requires:         R-CRAN-DT >= 0.11
Requires:         R-CRAN-mlr3learners 
Requires:         R-CRAN-mlr3pipelines 
Requires:         R-CRAN-mlr3viz 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-ggparty 
Requires:         R-CRAN-GGally 

%description
A web-based graphical user interface to provide the basic steps of a
machine learning workflow. It uses the functionalities of the 'mlr3'
framework.

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
