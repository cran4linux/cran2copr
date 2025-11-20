%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EcoCleanR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated and Controlled Extraction, Cleaning, and Processing of Occurrence Data for Generating Biogeographic Ranges of Marine Organisms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geodata 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mregions2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sdmpredictors 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geodata 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mregions2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sdmpredictors 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidyr 

%description
Provides step-by-step automation for integrating biodiversity data from
multiple online aggregators, merging and cleaning datasets while
addressing challenges such as taxonomic inconsistencies, georeferencing
issues, and spatial or environmental outliers. Includes functions to
extract environmental data and to define the biogeographic ranges in which
species are most likely to occur.

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
