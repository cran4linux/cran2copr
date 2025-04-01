%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adespatial
%global packver   0.3-27
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.27
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Multiscale Spatial Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ade4 >= 1.7.13
BuildRequires:    R-CRAN-adegraphics 
BuildRequires:    R-CRAN-adephylo 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ade4 >= 1.7.13
Requires:         R-CRAN-adegraphics 
Requires:         R-CRAN-adephylo 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-lattice 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-vegan 

%description
Tools for the multiscale spatial analysis of multivariate data. Several
methods are based on the use of a spatial weighting matrix and its
eigenvector decomposition (Moran's Eigenvectors Maps, MEM). Several
approaches are described in the review Dray et al (2012)
<doi:10.1890/11-1183.1>.

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
