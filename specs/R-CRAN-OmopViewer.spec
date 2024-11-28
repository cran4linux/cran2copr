%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OmopViewer
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualise OMOP Results using 'shiny' Applications

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-visOmopResults >= 0.5.0
BuildRequires:    R-CRAN-omopgenerics >= 0.4.0
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-styler 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-visOmopResults >= 0.5.0
Requires:         R-CRAN-omopgenerics >= 0.4.0
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-styler 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-yaml 

%description
Visualise results obtained from analysing data mapped to the Observational
Medical Outcomes Partnership (OMOP) common data model using 'shiny'
applications.

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
