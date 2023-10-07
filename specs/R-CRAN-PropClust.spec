%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PropClust
%global packver   1.4-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.7
Release:          1%{?dist}%{?buildtag}
Summary:          Propensity Clustering and Decomposition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-dynamicTreeCut 
BuildRequires:    R-stats 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-dynamicTreeCut 
Requires:         R-stats 

%description
Implementation of propensity clustering and decomposition as described in
Ranola et al. (2013) <doi:10.1186/1752-0509-7-21>. Propensity
decomposition can be viewed on the one hand as a generalization of the
eigenvector-based approximation of correlation networks, and on the other
hand as a generalization of random multigraph models and conformity-based
decompositions.

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
