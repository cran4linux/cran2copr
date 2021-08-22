%global __brp_check_rpaths %{nil}
%global packname  conmet
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Construct Measurement Evaluation Tool

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-waiter 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-summarytools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-semTools 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-waiter 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-summarytools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-semTools 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-DT 

%description
With this package you can run 'ConMET' locally in R. 'ConMET' is an
R-shiny application that facilitates performing and evaluating
confirmatory factor analyses (CFAs) and is useful for running and
reporting typical measurement models in applied psychology and management
journals. 'ConMET' automatically creates, compares and summarizes CFA
models. Most common fit indices (E.g., CFI and SRMR) are put in an
overview table. ConMET also allows to test for common method variance. The
application is particularly useful for teaching and instruction of
measurement issues in survey research. The application uses the 'lavaan'
package (Rosseel, 2012) to run CFAs.

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
