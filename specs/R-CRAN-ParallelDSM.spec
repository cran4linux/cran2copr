%global __brp_check_rpaths %{nil}
%global packname  ParallelDSM
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Digital Soil Mapping using Machine Learning

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-quantregForest 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-stats 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-pryr 
Requires:         R-utils 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-quantregForest 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rgdal 
Requires:         R-stats 

%description
Parallel computing, multi-core CPU is used to efficiently compute and
process multi-dimensional soil data.This package includes the parallelized
'Quantile Regression Forests' algorithm for Digital Soil Mapping and is
mainly dependent on the package 'quantregForest' and 'snowfall'. Detailed
references to the R package and the web site are described in the methods,
as detailed in the method documentation.

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
