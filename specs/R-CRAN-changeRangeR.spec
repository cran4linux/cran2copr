%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  changeRangeR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Change Metrics for Species Geographic Ranges

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rangeModelMetadata 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-phylobase 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rangeModelMetadata 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 

%description
Facilitates workflows to reproducibly transform estimates of species’
distributions into metrics relevant for conservation. For example,
combining predictions from species distribution models with other maps of
environmental data to characterize the proportion of a species’ range that
is under protection, calculating metrics used under the IUCN Criteria A
and B guidelines (Area of Occupancy and Extent of Occurrence), and
calculating more general metrics such as taxonomic and phylogenetic
diversity, as well as endemism. Also facilitates temporal comparisons
among biodiversity metrics to inform efforts towards complementarity and
consideration of future scenarios in conservation decisions.
'changeRangeR' also provides tools to determine the effects of modeling
decisions through sensitivity tests.

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
