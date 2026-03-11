%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wdnet
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted and Directed Networks

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildRequires:    R-CRAN-igraph >= 2.2.2
BuildRequires:    R-CRAN-CVXR >= 1.8.1
BuildRequires:    R-CRAN-Matrix >= 1.7.4
BuildRequires:    R-CRAN-wdm >= 0.2.6
BuildRequires:    R-CRAN-rARPACK >= 0.11.0
BuildRequires:    R-CRAN-RcppXPtrUtils >= 0.1.3
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-igraph >= 2.2.2
Requires:         R-CRAN-CVXR >= 1.8.1
Requires:         R-CRAN-Matrix >= 1.7.4
Requires:         R-CRAN-wdm >= 0.2.6
Requires:         R-CRAN-rARPACK >= 0.11.0
Requires:         R-CRAN-RcppXPtrUtils >= 0.1.3
Requires:         R-stats 

%description
Assortativity coefficients, centrality measures, and clustering
coefficients for weighted and directed networks. Rewiring unweighted
networks with given assortativity coefficients. Generating general
preferential attachment networks.

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
