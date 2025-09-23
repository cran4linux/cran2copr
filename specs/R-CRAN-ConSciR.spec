%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ConSciR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Conservation Science

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-padr 
BuildRequires:    R-CRAN-openair 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-padr 
Requires:         R-CRAN-openair 

%description
Provides data science tools for conservation science, including methods
for environmental data analysis, humidity calculations, sustainability
metrics, engineering calculations, and data visualisation. Supports
conservators, scientists, and engineers working with cultural heritage
preventive conservation data. The package is motivated by the framework
outlined in Cosaert and Beltran et al. (2022) "Tools for the Analysis of
Collection Environments"
<https://www.getty.edu/conservation/publications_resources/pdf_publications/tools_for_the_analysis_of_collection_environments.html>.

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
