%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bdc
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Biodiversity Data Cleaning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 1.0.5
BuildRequires:    R-CRAN-taxadb >= 0.1.3
BuildRequires:    R-CRAN-CoordinateCleaner 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-qs2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rgnparser 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-sf >= 1.0.5
Requires:         R-CRAN-taxadb >= 0.1.3
Requires:         R-CRAN-CoordinateCleaner 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-here 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-qs2 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rgnparser 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
It brings together several aspects of biodiversity data-cleaning in one
place. 'bdc' is organized in thematic modules related to different
biodiversity dimensions, including 1) Merge datasets: standardization and
integration of different datasets; 2) pre-filter: flagging and removal of
invalid or non-interpretable information, followed by data amendments; 3)
taxonomy: cleaning, parsing, and harmonization of scientific names from
several taxonomic groups against taxonomic databases locally stored
through the application of exact and partial matching algorithms; 4)
space: flagging of erroneous, suspect, and low-precision geographic
coordinates; and 5) time: flagging and, whenever possible, correction of
inconsistent collection date. In addition, it contains features to
visualize, document, and report data quality – which is essential for
making data quality assessment transparent and reproducible. The reference
for the methodology is Ribeiro and colleagues (2022)
<doi:10.1111/2041-210X.13868>.

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
