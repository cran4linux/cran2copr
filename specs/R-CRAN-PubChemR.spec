%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PubChemR
%global packver   0.99-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the 'PubChem' Database for Chemical Data Retrieval

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 

%description
Provides an R interface to the 'PubChem' database, which is a repository
for chemical information and a resource for finding chemical and
biological data. The package simplifies the process of retrieving and
handling chemical compound information from 'PubChem'. Users can search
for compounds, retrieve standard chemical information, download data in
various formats, and query the database using the 'PubChem' Power User
Gateway (PUG) 'RESTful' API
<https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest>. The package aims to
facilitate the integration of chemical data in bioinformatics and
cheminformatics workflows.

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
