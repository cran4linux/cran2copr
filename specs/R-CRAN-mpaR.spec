%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mpaR
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Main Path Analysis for Citation and Directed Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-igraph >= 1.3.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-CRAN-xml2 

%description
Implements Main Path Analysis (MPA) as introduced by Hummon and Doreian
(1989) <doi:10.1016/0378-8733(89)90017-8>. Given a directed acyclic graph
(DAG) representing a citation or precedence network, the package computes
traversal weights (SPC, SPLC, SPNP) for each edge and extracts the global,
local, and key-route main paths. Also provides tools for DAG validation,
node role classification (source/terminal/user), per-component path
extraction for disconnected networks, and scale-free network testing.
Accepts 'igraph' objects or edge-list data frames as input. Includes
readers for 'Pajek' (.net) and 'Gephi' export (.gexf, .graphml) files.

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
