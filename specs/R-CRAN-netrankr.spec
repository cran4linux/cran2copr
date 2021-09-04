%global __brp_check_rpaths %{nil}
%global packname  netrankr
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Partial Rankings in Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-CRAN-Matrix 

%description
Implements methods for centrality related analyses of networks. While the
package includes the possibility to build more than 20 indices, its main
focus lies on index-free assessment of centrality via partial rankings
obtained by neighborhood-inclusion or positional dominance. These partial
rankings can be analyzed with different methods, including probabilistic
methods like computing expected node ranks and relative rank probabilities
(how likely is it that a node is more central than another?). The
methodology is described in depth in the vignettes and in Schoch (2018)
<doi:10.1016/j.socnet.2017.12.003>.

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
