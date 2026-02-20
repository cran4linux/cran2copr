%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  manynet
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Many Ways to Make, Modify, Mark, and Measure Myriad Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 2.1.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-tidygraph 
Requires:         R-CRAN-igraph >= 2.1.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-network 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-tidygraph 

%description
Many tools for making, modifying, marking, measuring, and motifs and
memberships of many different types of networks. All functions operate
with matrices, edge lists, and 'igraph', 'network', and 'tidygraph'
objects, on directed, multiplex, multimodal, signed, and other networks.
The package includes functions for importing and exporting, creating and
generating networks, modifying networks and node and tie attributes, and
describing networks with sensible defaults.

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
