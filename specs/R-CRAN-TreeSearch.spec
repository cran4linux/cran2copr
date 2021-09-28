%global __brp_check_rpaths %{nil}
%global packname  TreeSearch
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Tree Search Using Custom Optimality Criteria

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ape >= 5.1
BuildRequires:    R-CRAN-cli >= 3.0
BuildRequires:    R-CRAN-phangorn >= 2.2.1
BuildRequires:    R-CRAN-TreeTools >= 1.5.0
BuildRequires:    R-CRAN-fastmatch >= 1.1.3
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-TreeDist > 2.0.3
BuildRequires:    R-CRAN-Rogue > 1.0.0
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-protoclust 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
Requires:         R-CRAN-ape >= 5.1
Requires:         R-CRAN-cli >= 3.0
Requires:         R-CRAN-phangorn >= 2.2.1
Requires:         R-CRAN-TreeTools >= 1.5.0
Requires:         R-CRAN-fastmatch >= 1.1.3
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-TreeDist > 2.0.3
Requires:         R-CRAN-Rogue > 1.0.0
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-future 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-protoclust 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 

%description
Search for phylogenetic trees that are optimal using a user-defined
criterion. Contains a "shiny" user interface for interactive tree search
and exploration of results, including character visualization, rogue taxon
detection, tree space mapping, and cluster consensus trees. Handles
inapplicable data using the algorithm of Brazeau, Guillerme and Smith
(2019) <doi:10.1093/sysbio/syy083> using the "Morphy" library. Implements
Profile Parsimony (Faith and Trueman, 2001) <doi:10.1080/10635150118627>,
and Successive Approximations (Farris, 1969) <doi:10.2307/2412182>.

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
