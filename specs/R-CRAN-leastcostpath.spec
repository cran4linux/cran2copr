%global __brp_check_rpaths %{nil}
%global packname  leastcostpath
%global packver   1.8.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.7
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling Pathways and Movement Potential Within a Landscape

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.4.1
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-pbapply >= 1.4.2
BuildRequires:    R-CRAN-rgdal >= 1.3.3
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-gdistance >= 1.2.2
BuildRequires:    R-CRAN-rgeos >= 0.3.28
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-gstat 
Requires:         R-parallel >= 3.4.1
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-pbapply >= 1.4.2
Requires:         R-CRAN-rgdal >= 1.3.3
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-gdistance >= 1.2.2
Requires:         R-CRAN-rgeos >= 0.3.28
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-gstat 

%description
Calculates cost surfaces based on slope to be used when modelling pathways
and movement potential within a landscape (Lewis, 2021)
<doi:10.1007/s10816-021-09522-w>.

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
