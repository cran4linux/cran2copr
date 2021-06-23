%global __brp_check_rpaths %{nil}
%global packname  ontoFAST
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Annotation of Characters with Biological Ontologies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ontologyIndex 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sunburstR 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ontologyIndex 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sunburstR 
Requires:         R-CRAN-usethis 

%description
Tools for annotating characters (character matrices) with anatomical and
phenotype ontologies. Includes functions for visualising character
annotations and creating simple queries using ontological relationships.

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
