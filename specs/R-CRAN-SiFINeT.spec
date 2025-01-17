%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SiFINeT
%global packver   1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Single Cell Feature Identification with Network Topology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-quantreg >= 5.94
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-ggraph >= 2.0.6
BuildRequires:    R-CRAN-Matrix >= 1.5.1
BuildRequires:    R-CRAN-igraph >= 1.3.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-quantreg >= 5.94
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-ggraph >= 2.0.6
Requires:         R-CRAN-Matrix >= 1.5.1
Requires:         R-CRAN-igraph >= 1.3.5
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 

%description
Cluster-independent method based on topology structure of gene
co-expression network for identifying feature gene sets, extracting
cellular subpopulations, and elucidating intrinsic relationships among
these subpopulations. Without prior cell clustering, SifiNet circumvents
potential inaccuracies in clustering that may influence subsequent
analyses. This method is introduced in Qi Gao, Zhicheng Ji, Liuyang Wang,
Kouros Owzar, Qi-Jing Li, Cliburn Chan, Jichun Xie "SifiNet: a robust and
accurate method to identify feature gene sets and annotate cells" (2024)
<doi:10.1093/nar/gkae307>.

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
