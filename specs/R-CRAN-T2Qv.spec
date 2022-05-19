%global __brp_check_rpaths %{nil}
%global packname  T2Qv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Control Qualitative Variables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools >= 0.5.1.1
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ca 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tables 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-htmltools >= 0.5.1.1
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ca 
Requires:         R-CRAN-highcharter 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tables 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 

%description
Covers k-table control analysis using multivariate control charts for
qualitative variables using fundamentals of multiple correspondence
analysis and multiple factor analysis. The graphs can be shown in a flat
or interactive way, in the same way all the outputs can be shown in an
interactive shiny panel.

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
