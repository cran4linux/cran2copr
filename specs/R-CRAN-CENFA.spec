%global __brp_check_rpaths %{nil}
%global packname  CENFA
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Climate and Ecological Niche Factor Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-parallel >= 3.3.3
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-pbapply >= 1.3.3
BuildRequires:    R-CRAN-sp >= 1.2.7
BuildRequires:    R-CRAN-doSNOW >= 1.0.16
BuildRequires:    R-CRAN-snow >= 0.4.2
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-parallel >= 3.3.3
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-pbapply >= 1.3.3
Requires:         R-CRAN-sp >= 1.2.7
Requires:         R-CRAN-doSNOW >= 1.0.16
Requires:         R-CRAN-snow >= 0.4.2
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Tools for climate- and ecological-niche factor analysis of spatial data,
including methods for visualization of spatial variability of species
sensitivity, exposure, and vulnerability to climate change. Processing of
large files and parallel methods are supported. Climate-niche factor
analysis is described in Rinnan and Lawler (2019)
<doi:10.1111/ecog.03937>.

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
