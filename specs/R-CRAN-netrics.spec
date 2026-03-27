%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  netrics
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Many Ways to Measure and Classify Membership for Networks, Nodes, and Ties

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 2.1.0
BuildRequires:    R-CRAN-manynet 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-igraph >= 2.1.0
Requires:         R-CRAN-manynet 
Requires:         R-CRAN-dplyr 

%description
Many tools for calculating network, node, or tie marks, measures, motifs
and memberships of many different types of networks. Marks identify
structural positions, measures quantify network properties, memberships
classify nodes into groups, and motifs tabulate substructure
participation. All functions operate with all classes of network data
covered in 'manynet', and on directed, undirected, multiplex, multimodal,
signed, and other networks.

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
