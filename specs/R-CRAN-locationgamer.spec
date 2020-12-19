%global packname  locationgamer
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Identification of Location Game Equilibria in Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
Requires:         R-graphics 

%description
Identification of equilibrium locations in location games (Hotelling
(1929) <doi:10.2307/2224214>). In these games, two competing actors place
customer-serving units in two locations simultaneously. Customers make the
decision to visit the location that is closest to them. The functions in
this package include Prim algorithm (Prim (1957)
<doi:10.1002/j.1538-7305.1957.tb01515.x>) to find the minimum spanning
tree connecting all network vertices, an implementation of Dijkstra
algorithm (Dijkstra (1959) <doi:10.1007/BF01386390>) to find the shortest
distance and path between any two vertices, a self-developed algorithm
using elimination of purely dominated strategies to find the equilibrium,
and several plotting functions.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
