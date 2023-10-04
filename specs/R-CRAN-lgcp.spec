%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lgcp
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Log-Gaussian Cox Process

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rpanel >= 1.1.3
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.utils 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-rpanel >= 1.1.3
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.utils 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-raster 
Requires:         R-tcltk 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-ncdf4 
Requires:         R-methods 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-Matrix 

%description
Spatial and spatio-temporal modelling of point patterns using the
log-Gaussian Cox process. Bayesian inference for spatial, spatiotemporal,
multivariate and aggregated point processes using Markov chain Monte
Carlo. See Benjamin M. Taylor, Tilman M. Davies, Barry S. Rowlingson,
Peter J. Diggle (2015) <doi:10.18637/jss.v063.i07>.

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
