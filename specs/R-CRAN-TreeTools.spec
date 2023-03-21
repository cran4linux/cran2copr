%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TreeTools
%global packver   1.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create, Modify and Analyse Phylogenetic Trees

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ape >= 5.6
BuildRequires:    R-CRAN-Rdpack >= 2.3
BuildRequires:    R-CRAN-fastmatch >= 1.1.3
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ape >= 5.6
Requires:         R-CRAN-Rdpack >= 2.3
Requires:         R-CRAN-fastmatch >= 1.1.3
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-colorspace 
Requires:         R-methods 
Requires:         R-CRAN-R.cache 

%description
Efficient implementations of functions for the creation, modification and
analysis of phylogenetic trees. Applications include: generation of trees
with specified shapes; tree rearrangement; analysis of tree shape; rooting
of trees and extraction of subtrees; calculation and depiction of split
support; plotting the position of rogue taxa (Klopfstein & Spasojevic
2019) <doi:10.1371/journal.pone.0212942>; calculation of
ancestor-descendant relationships, of 'stemwardness' (Asher & Smith, 2022)
<doi:10.1093/sysbio/syab072>, and of tree balance (Mir et al. 2013)
<doi:10.1016/j.mbs.2012.10.005>; artificial extinction (Asher & Smith,
2022) <doi:10.1093/sysbio/syab072>; import and export of trees from
Newick, Nexus (Maddison et al. 1997) <doi:10.1093/sysbio/46.4.590>, and
TNT <https://www.lillo.org.ar/phylogeny/tnt/> formats; and analysis of
splits and cladistic information.

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
