%global __brp_check_rpaths %{nil}
%global packname  leidenAlg
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Implements the Leiden Algorithm via an R Interface

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix.utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-sccore 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix.utils 
Requires:         R-parallel 
Requires:         R-CRAN-sccore 
Requires:         R-stats 

%description
An R interface to the Leiden algorithm, an iterative community detection
algorithm on networks. The algorithm is designed to converge to a
partition in which all subsets of all communities are locally optimally
assigned, yielding communities guaranteed to be connected. The
implementation proves to be fast, scales well, and can be run on graphs of
millions of nodes (as long as they can fit in memory). The original
implementation was constructed as a python interface "leidenalg" found
here: <https://github.com/vtraag/leidenalg>. The algorithm was originally
described in Traag, V.A., Waltman, L. & van Eck, N.J. "From Louvain to
Leiden: guaranteeing well-connected communities". Sci Rep 9, 5233 (2019)
<doi:10.1038/s41598-019-41695-z>.

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
