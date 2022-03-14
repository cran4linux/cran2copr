%global __brp_check_rpaths %{nil}
%global packname  BAT
%global packver   2.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Biodiversity Assessment Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-hypervolume 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-geometry 
Requires:         R-graphics 
Requires:         R-CRAN-hypervolume 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-nls2 
Requires:         R-parallel 
Requires:         R-CRAN-raster 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vegan 

%description
Includes algorithms to assess alpha and beta diversity in all their
dimensions (taxonomic, phylogenetic and functional). It allows performing
a number of analyses based on species identities/abundances,
phylogenetic/functional distances, trees, convex-hulls or kernel density
n-dimensional hypervolumes depicting species relationships. Cardoso et al.
(2015) <doi:10.1111/2041-210X.12310>.

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
