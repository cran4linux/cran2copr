%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  caretSDM
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Build Species Distribution Modeling using 'caret'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-blockCV 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-CoordinateCleaner 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ecospat 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggspatial 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-mapview 
BuildRequires:    R-CRAN-maxnet 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-pdp 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-usdm 
BuildRequires:    R-utils 
Requires:         R-CRAN-blockCV 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-CoordinateCleaner 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ecospat 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggspatial 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-mapview 
Requires:         R-CRAN-maxnet 
Requires:         R-methods 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-pdp 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-stats 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-usdm 
Requires:         R-utils 

%description
Use machine learning algorithms and advanced geographic information system
tools to build Species Distribution Modeling in a extensible and modern
fashion.

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
