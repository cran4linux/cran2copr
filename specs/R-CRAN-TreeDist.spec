%global __brp_check_rpaths %{nil}
%global packname  TreeDist
%global packver   2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate and Map Distances Between Phylogenetic Trees

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-cli >= 3.0
BuildRequires:    R-CRAN-phangorn >= 2.2.1
BuildRequires:    R-CRAN-TreeTools >= 1.7.0
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-cli >= 3.0
Requires:         R-CRAN-phangorn >= 2.2.1
Requires:         R-CRAN-TreeTools >= 1.7.0
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-stats 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 

%description
Implements measures of tree similarity, including information-based
generalized Robinson-Foulds distances (Phylogenetic Information Distance,
Clustering Information Distance, Matching Split Information Distance;
Smith 2020) <doi:10.1093/bioinformatics/btaa614>; Jaccard-Robinson-Foulds
distances (Bocker et al. 2013) <doi:10.1007/978-3-642-40453-5_13>,
including the Nye et al. (2006) metric
<doi:10.1093/bioinformatics/bti720>; the Matching Split Distance
(Bogdanowicz & Giaro 2012) <doi:10.1109/TCBB.2011.48>; Maximum Agreement
Subtree distances; the Kendall-Colijn (2016) distance
<doi:10.1093/molbev/msw124>, and the Nearest Neighbour Interchange (NNI)
distance, approximated per Li et al. (1996)
<doi:10.1007/3-540-61332-3_168>. Includes tools for visualizing mappings
of tree space (Smith 2022) <doi:10.1093/sysbio/syab100>, for calculating
the median of sets of trees, and for computing the information content of
trees and splits.

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
