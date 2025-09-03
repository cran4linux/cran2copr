%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcaiman
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          CAnopy IMage ANalysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-filenamer 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-spatial 
BuildRequires:    R-CRAN-lidR 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-filenamer 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-terra 
Requires:         R-methods 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-spatial 
Requires:         R-CRAN-lidR 
Requires:         R-tcltk 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Tools for preprocessing and processing canopy photographs with support for
raw data reading. Provides methods to address variability in sky
brightness and to mitigate errors from image acquisition in non-diffuse
light. Works with all types of fish-eye lenses, and some methods also
apply to conventional lenses.

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
