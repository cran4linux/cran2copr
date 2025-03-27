%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSNbler
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Assemble 'SSN' Objects

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-SSN2 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-pdist 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-SSN2 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
Import, create and assemble data needed to fit spatial-statistical
stream-network models using the 'SSN2' package for 'R'. Streams,
observations, and prediction locations are represented as simple features
and specific tools provided to define topological relationships between
features; calculate the hydrologic distances (with flow-direction
preserved) and the spatial additive function used to weight converging
stream segments; and export the topological, spatial, and attribute
information to an `SSN` (spatial stream network) object, which can be
efficiently stored, accessed and analysed in 'R'. A detailed description
of methods used to calculate and format the spatial data can be found in
Peterson, E.E. and Ver Hoef, J.M., (2014) <doi:10.18637/jss.v056.i02>.

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
