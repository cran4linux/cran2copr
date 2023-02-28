%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSN
%global packver   1.1.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.17
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Modeling on Stream Networks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-rgdal >= 1.2.5
BuildRequires:    R-CRAN-RSQLite >= 1.1.2
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-rgeos >= 0.3.22
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-rgdal >= 1.2.5
Requires:         R-CRAN-RSQLite >= 1.1.2
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-rgeos >= 0.3.22
Requires:         R-CRAN-sp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-lattice 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 

%description
Spatial statistical modeling and prediction for data on stream networks,
including models based on in-stream distance (Ver Hoef, J.M. and Peterson,
E.E., 2010. <DOI:10.1198/jasa.2009.ap08248>.) Models are created using
moving average constructions. Spatial linear models, including explanatory
variables, can be fit with (restricted) maximum likelihood.  Mapping and
other graphical functions are included.

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
