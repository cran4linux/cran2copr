%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OhdsiShinyAppBuilder
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Viewing Observational Health Data Sciences and Informatics Results via 'shiny' Modules

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ParallelLogger >= 2.0.0
BuildRequires:    R-CRAN-ResultModelManager >= 0.4.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-DatabaseConnector 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-utils 
Requires:         R-CRAN-ParallelLogger >= 2.0.0
Requires:         R-CRAN-ResultModelManager >= 0.4.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-DatabaseConnector 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-utils 

%description
Users can build a single 'shiny' app for exploring population
characterization, population-level causal effect estimation, and
patient-level prediction results generated via the R analyses packages in
'HADES' (see <https://ohdsi.github.io/Hades/>). Learn more about
'OhdsiShinyAppBuilder' at <https://ohdsi.github.io/OhdsiShinyAppBuilder/>.

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
