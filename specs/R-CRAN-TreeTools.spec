%global packname  TreeTools
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create, Modify and Analyse Phylogenetic Trees

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-phangorn >= 2.2.1
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-phangorn >= 2.2.1
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-R.cache 
Requires:         R-CRAN-Rdpack 

%description
Efficient implementations of functions for the creation, modification and
analysis of phylogenetic trees. Applications include: generation of trees
with specified shapes; analysis of tree shape; rooting of trees and
extraction of subtrees; calculation and depiction of node support;
calculation of ancestor-descendant relationships; import and export of
trees from Newick, Nexus (Maddison et al. 1997)
<doi:10.1093/sysbio/46.4.590>, and TNT
<http://www.lillo.org.ar/phylogeny/tnt/> formats; and analysis of splits
and cladistic information.

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
