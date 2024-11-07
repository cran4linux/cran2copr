%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rpolyhedra
%global packver   0.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          Polyhedra Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-lgr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 

%description
A polyhedra database scraped from various sources as R6 objects and 'rgl'
visualizing capabilities.

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
