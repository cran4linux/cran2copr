%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  htna
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Heterogeneous Transition Network Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Nestimate 
BuildRequires:    R-CRAN-cograph 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-Nestimate 
Requires:         R-CRAN-cograph 
Requires:         R-CRAN-igraph 

%description
Implements the Heterogeneous Transition Network Analysis (HTNA) method
described by López-Pernas et al. (2026) <doi:10.1002/jcal.70285>. The
method is an extension of transition network analysis (TNA) where actions
or events belong to two or more distinct actor types (e.g. Human and
AI),preserving the actor type partition on the resulting network. Provides
a thin, focused API on top of the 'Nestimate' estimation engine and the
'cograph' rendering engine, so downstream bootstrap, permutation,
reliability, centrality, and plotting functions treat each actor's codes
as a distinct node group.

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
