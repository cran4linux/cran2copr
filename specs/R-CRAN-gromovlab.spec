%global __brp_check_rpaths %{nil}
%global packname  gromovlab
%global packver   0.8-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          Gromov-Hausdorff Type Distances for Labeled Metric Spaces

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-glpkAPI 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-glpkAPI 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-cluster 
Requires:         R-stats 

%description
Computes Gromov-Hausdorff type l^p distances for labeled metric spaces.
These distances were introduced in V.Liebscher, Gromov meets Phylogenetics
- new Animals for the Zoo of Metrics on Tree Space <arXiv:1504.05795> for
phylogenetic trees, but may apply to a diversity of scenarios.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
