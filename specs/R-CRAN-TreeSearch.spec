%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TreeSearch
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Analysis with Discrete Character Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-ape >= 5.6
BuildRequires:    R-CRAN-cli >= 3.0
BuildRequires:    R-CRAN-TreeDist >= 2.6.3
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-TreeTools >= 1.10.0
BuildRequires:    R-CRAN-fastmatch >= 1.1.3
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-Rogue > 2.0.0
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-PlotTools 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-protoclust 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
Requires:         R-CRAN-ape >= 5.6
Requires:         R-CRAN-cli >= 3.0
Requires:         R-CRAN-TreeDist >= 2.6.3
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-TreeTools >= 1.10.0
Requires:         R-CRAN-fastmatch >= 1.1.3
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-Rogue > 2.0.0
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-future 
Requires:         R-CRAN-PlotTools 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-protoclust 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 

%description
Reconstruct phylogenetic trees from discrete data. Inapplicable character
states are handled using the algorithm of Brazeau, Guillerme and Smith
(2019) <doi:10.1093/sysbio/syy083> with the "Morphy" library, under equal
or implied step weights. Contains a "shiny" user interface for interactive
tree search and exploration of results, including character visualization,
rogue taxon detection, tree space mapping, and cluster consensus trees
(Smith 2022a, b) <doi:10.1093/sysbio/syab099>,
<doi:10.1093/sysbio/syab100>. Profile Parsimony (Faith and Trueman, 2001)
<doi:10.1080/10635150118627>, Successive Approximations (Farris, 1969)
<doi:10.2307/2412182> and custom optimality criteria are implemented.

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
