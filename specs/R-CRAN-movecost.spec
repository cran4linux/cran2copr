%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  movecost
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculation of Slope-Dependant Accumulated Cost Surface, Least-Cost Paths, Least-Cost Corridors, Least-Cost Networks Related to Human Movement Across the Landscape

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-terra >= 1.7.0
BuildRequires:    R-CRAN-igraph >= 1.4.0
BuildRequires:    R-CRAN-sf >= 1.0.9
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-terra >= 1.7.0
Requires:         R-CRAN-igraph >= 1.4.0
Requires:         R-CRAN-sf >= 1.0.9
Requires:         R-utils 
Requires:         R-grDevices 

%description
Provides the facility to calculate non-isotropic accumulated cost
surfaces, least-cost paths, least-cost corridors, least-cost networks,
ranked alternative paths, cost allocation and cost boundaries, using a
number of human-movement-related cost functions that can be selected by
the user. The package is built around a compute-once design: a single cost
surface object is created first and then reused by every analysis
function, avoiding redundant computation. Visualisation is fully decoupled
from computation and is provided through 'ggplot2' methods that can be
invoked, customised, and re-invoked at any time without re-running any
analysis. It just requires a Digital Terrain Model, a start location and
(optionally) destination locations. See Alberti (2019)
<doi:10.1016/j.softx.2019.100331>.

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
