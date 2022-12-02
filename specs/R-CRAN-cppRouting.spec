%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cppRouting
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithms for Routing and Solving the Traffic Assignment Problem

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-data.table 

%description
Calculation of distances, shortest paths and isochrones on weighted graphs
using several variants of Dijkstra algorithm. Proposed algorithms are
unidirectional Dijkstra (Dijkstra, E. W. (1959) <doi:10.1007/BF01386390>),
bidirectional Dijkstra (Goldberg, Andrew & Fonseca F. Werneck, Renato
(2005)
<https://archive.siam.org/meetings/alenex05/papers/03agoldberg.pdf>), A*
search (P. E. Hart, N. J. Nilsson et B. Raphael (1968)
<doi:10.1109/TSSC.1968.300136>), new bidirectional A* (Pijls & Post (2009)
<https://repub.eur.nl/pub/16100/ei2009-10.pdf>), Contraction hierarchies
(R. Geisberger, P. Sanders, D. Schultes and D. Delling (2008)
<doi:10.1007/978-3-540-68552-4_24>), PHAST (D. Delling, A.Goldberg, A.
Nowatzyk, R. Werneck (2011) <doi:10.1016/j.jpdc.2012.02.007>). Algorithms
for solving the traffic assignment problem are All-or-Nothing assignment,
Method of Successive Averages, Frank-Wolfe algorithm (M. Fukushima (1984)
<doi:10.1016/0191-2615(84)90029-8>), Conjugate and Bi-Conjugate
Frank-Wolfe algorithms (M. Mitradjieva, P. O. Lindberg (2012)
<doi:10.1287/trsc.1120.0409>), Algorithm-B (R. B. Dial (2006)
<doi:10.1016/j.trb.2006.02.008>).

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
