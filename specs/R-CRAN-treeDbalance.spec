%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  treeDbalance
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of 3D Tree Imbalance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-R.matlab 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-R.matlab 

%description
The main goal of the R package 'treeDbalance' is to provide functions for
the computation of several measurements of 3D node imbalance and their
respective 3D tree imbalance indices, as well as to introduce the new
'phylo3D' format for rooted 3D tree objects. Moreover, it encompasses an
example dataset of 3D models of 63 beans in 'phylo3D' format. Please note
that this R package was developed alongside the project described in the
manuscript 'Measuring 3D tree imbalance of plant models using
graph-theoretical approaches' by M. Fischer, S. Kersting, and L. Kühn
(2023) <doi:10.48550/arXiv.2307.14537>, which provides precise
mathematical definitions of the measurements. Furthermore, the package
contains several helpful functions, for example, some auxiliary functions
for computing the ancestors, descendants, and depths of the nodes, which
ensures that the computations can be done in linear time, or functions
that convert existing formats of 3D tree models of other software into the
'phylo3D' format. Moreover, it comprises functions to extract the
graph-theoretical topology without vertices of in- and out-degree 1 of
rooted 3D trees as well as to adapt node enumerations to the common
'phylo' format. Most functions of 'treeDbalance' require as input a rooted
tree in the 'phylo3D' format, an extended 'phylo' format (as introduced in
the R package 'ape' 1.9 in November 2006). Such a 'phylo3D' object must
have at least two new attributes next to those required by the 'phylo'
format: 'node.coord', the coordinates of the nodes, as well as
'edge.weight', the literal weight or volume of the edges. Optional
attributes are 'edge.diam', the diameter of the edges, and 'edge.length',
the length of the edges. For visualization purposes one can also specify
'edge.type', which ranges from normal cylinder to bud to leaf, as well as
'edge.color' to change the color of the edge depiction. This project was
supported by the joint research project DIG-IT! funded by the European
Social Fund (ESF), reference: ESF/14-BM-A55-0017/19, and the Ministry of
Education, Science and Culture of Mecklenburg-Western Pomerania, Germany,
as well as by the project ArtIGROW, which is a part of the WIR!-Alliance
'ArtIFARM – Artificial Intelligence in Farming' funded by the German
Federal Ministry of Education and Research (FKZ: 03WIR4805).

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
