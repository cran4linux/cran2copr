%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BeeBDC
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Occurrence Data Cleaning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-CoordinateCleaner 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggspatial 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-mgsub 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-paletteer 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-CoordinateCleaner 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggspatial 
Requires:         R-CRAN-here 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-mgsub 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-paletteer 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 

%description
Flags and checks occurrence data that are in Darwin Core format.  The
package includes generic functions and data as well as some that are
specific to bees. This package is meant to build upon and be complimentary
to other excellent occurrence cleaning packages, including 'bdc' and
'CoordinateCleaner'.  This package uses datasets from several sources and
particularly from the Discover Life Website, created by Ascher and
Pickering (2020).  For further information, please see the original
publication and package website.  Publication - Dorey et al. (2023)
<doi:10.1101/2023.06.30.547152> and package website - Dorey et al. (2023)
<https://github.com/jbdorey/BeeBDC>.

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
