%global __brp_check_rpaths %{nil}
%global packname  treebalance
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Tree (Im)Balance Indices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-memoise 

%description
The aim of the 'R' package 'treebalance' is to provide functions for the
computation of a large variety of (im)balance indices for rooted trees.
The package accompanies the manuscript ''Tree balance indices: a
comprehensive survey'' by M. Fischer, L. Herbst, S. Kersting, L. Kuehn and
K. Wicke (2021) <arXiv:2109.12281>, which gives a precise definition for
the terms 'balance index' and 'imbalance index' (Section 3) and provides
an overview of the terminology in this manual (Section 2). For further
information on (im)balance indices, see also Fischer et al. (2021)
<https://treebalance.wordpress.com>. Considering both established and new
(im)balance indices, 'treebalance' provides (among others) functions for
calculating the following 18 established indices: the average leaf depth,
the B1 and B2 index, the Colijn-Plazzotta rank, the normal, corrected,
quadratic and equal weights Colless index, the family of Colless-like
indices, the family of I-based indices, the Rogers J index, the Furnas
rank, the rooted quartet index, the s-shape statistic, the Sackin index,
the symmetry nodes index, the total cophenetic index and the variance of
leaf depths. Additionally, we include 5 tree shape statistics that satisfy
the definition of an (im)balance index but have not been thoroughly
analyzed in terms of tree balance in the literature yet. These are: the
maximum width, the maximum difference in widths, the maximal depth, the
stairs1 and the stairs2 index. As input, most functions of 'treebalance'
require a rooted (phylogenetic) tree in 'phylo' format (as introduced in
'ape' 1.9 in November 2006). 'phylo' is used to store (phylogenetic) trees
with no vertices of out-degree one. For further information on the format
we kindly refer the reader to E. Paradis (2012)
<http://ape-package.ird.fr/misc/FormatTreeR_24Oct2012.pdf>.

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
