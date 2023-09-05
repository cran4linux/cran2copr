%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wdnet
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted and Directed Networks

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-RcppXPtrUtils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wdm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-RcppXPtrUtils 
Requires:         R-stats 
Requires:         R-CRAN-wdm 

%description
Implementations of network analysis including (1) assortativity
coefficient of weighted and directed networks, Yuan, Yan and Zhang (2021)
<doi:10.1093/comnet/cnab017>, (2) centrality measures for weighted and
directed networks, Opsahl, Agneessens and Skvoretz (2010)
<doi:10.1016/j.socnet.2010.03.006>, Zhang, Wang and Yan (2022)
<doi:10.1016/j.physa.2021.126438>, (3) clustering coefficient of weighted
and directed networks, Fagiolo (2007) <doi:10.1103/PhysRevE.76.026107> and
Clemente and Grassi (2018) <doi:10.1016/j.chaos.2017.12.007>, (4) rewiring
networks with given assortativity coefficients, Wang, Yan, Yuan and Zhang
(2022) <doi:10.1007/s11222-022-10161-8>, (5) preferential attachment
network generation, Yuan, Wang, Yan and Zhang (2023)
<doi:10.6339/23-JDS1110>.

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
