%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  warehouseTools
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Heuristics for Solving the Traveling Salesman Problem in Warehouse Layouts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-clusterSim 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-clusterSim 

%description
Heuristic methods to solve the routing problems in a warehouse management.
Package includes several heuristics such as the Midpoint, Return, S-Shape
and Semi-Optimal Heuristics for designation of the picker’s route in order
picking. The heuristics aim to provide the acceptable travel distances
while considering warehouse layout constraints such as aisles and shelves.
It also includes implementation of the COPRAS (COmplex PRoportional
ASsessment) method for supporting selection of locations to be visited by
the picker in shared storage systems. The package is designed to
facilitate more efficient warehouse routing and logistics operations. see:
Bartholdi, J. J., Hackman, S. T. (2019). "WAREHOUSE & DISTRIBUTION
SCIENCE. Release 0.98.1." The Supply Chain & Logistics Institute. H.
Milton Stewart School of Industrial and Systems Engineering. Georgia
Institute of Technology.
<https://www.warehouse-science.com/book/editions/wh-sci-0.98.1.pdf>.

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
