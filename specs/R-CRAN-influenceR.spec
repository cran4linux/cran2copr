%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  influenceR
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Software Tools to Quantify Structural Importance of Nodes in a Network

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Matrix >= 1.1.4
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-Matrix >= 1.1.4
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-methods 
Requires:         R-utils 

%description
Provides functionality to compute various node centrality measures on
networks. Included are functions to compute betweenness centrality (by
utilizing Madduri and Bader's SNAP library), implementations of constraint
and effective network size by Burt (2000)
<doi:10.1016/S0191-3085(00)22009-1>; algorithm to identify key players by
Borgatti (2006) <doi:10.1007/s10588-006-7084-x>; and the bridging
algorithm by Valente and Fujimoto (2010)
<doi:10.1016/j.socnet.2010.03.003>. On Unix systems, the betweenness, Key
Players, and bridging implementations are parallelized with OpenMP, which
may run faster on systems which have OpenMP configured.

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
