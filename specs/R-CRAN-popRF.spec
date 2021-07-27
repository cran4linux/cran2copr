%global __brp_check_rpaths %{nil}
%global packname  popRF
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Random Forest-Informed Population Disaggregation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-quantregForest 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-raster 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-quantregForest 
Requires:         R-CRAN-plyr 

%description
Disaggregating census-based areal population counts to finer gridded
population surfaces using Random Forest algorithm to determine the target
area weights (see _Stevens, et al._ (2015)
<doi:10.1371/journal.pone.0107042>).

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
