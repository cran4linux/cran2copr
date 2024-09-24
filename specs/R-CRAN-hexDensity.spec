%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hexDensity
%global packver   1.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Kernel Density Estimation with Hexagonal Grid

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-methods 

%description
Kernel density estimation with hexagonal grid for bivariate data.
Hexagonal grid has many beneficial properties like equidistant neighbours
and less edge bias, making it better for spatial analyses than the more
commonly used rectangular grid. Carr, D. B. et al. (1987)
<doi:10.2307/2289444>. Diggle, P. J. (2010) <doi:10.1201/9781420072884>.
Hill, B. (2017) <https://blog.bruce-hill.com/meandering-triangles>. Jones,
M. C. (1993) <doi:10.1007/BF00147776>.

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
