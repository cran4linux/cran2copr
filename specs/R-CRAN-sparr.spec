%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sparr
%global packver   2.3-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.10
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial and Spatiotemporal Relative Risk

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 2.3.0
BuildRequires:    R-CRAN-spatstat.utils 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-misc3d 
Requires:         R-CRAN-spatstat >= 2.3.0
Requires:         R-CRAN-spatstat.utils 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-misc3d 

%description
Provides functions to estimate kernel-smoothed spatial and spatio-temporal
densities and relative risk functions, and perform subsequent inference.
Methodological details can be found in the accompanying tutorial: Davies
et al. (2018) <DOI:10.1002/sim.7577>.

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
