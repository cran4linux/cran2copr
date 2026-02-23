%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flownet
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Transport Modeling: Network Processing, Route Enumeration, and Traffic Assignment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-mirai >= 2.5.2
BuildRequires:    R-CRAN-collapse >= 2.1.5
BuildRequires:    R-CRAN-igraph >= 2.1.4
BuildRequires:    R-CRAN-leaderCluster >= 1.5
BuildRequires:    R-CRAN-progress >= 1.2.3
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-geodist >= 0.1.1
BuildRequires:    R-CRAN-kit >= 0.0.21
Requires:         R-CRAN-mirai >= 2.5.2
Requires:         R-CRAN-collapse >= 2.1.5
Requires:         R-CRAN-igraph >= 2.1.4
Requires:         R-CRAN-leaderCluster >= 1.5
Requires:         R-CRAN-progress >= 1.2.3
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-geodist >= 0.1.1
Requires:         R-CRAN-kit >= 0.0.21

%description
High-performance tools for transport modeling - network processing, route
enumeration, and traffic assignment in R. The package implements the
Path-Sized Logit model for traffic assignment - Ben-Akiva and Bierlaire
(1999) <doi:10.1007/978-1-4615-5203-1_2> - an efficient route enumeration
algorithm, and provides powerful utility functions for (multimodal)
network generation, consolidation/contraction, and/or simplification. The
user is expected to provide a transport network (either a graph or
collection of linestrings) and an origin-destination (OD) matrix of
trade/traffic flows. Maintained by transport consultants at CPCS
(cpcs.ca).

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
