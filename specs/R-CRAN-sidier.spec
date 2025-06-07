%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sidier
%global packver   4.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Substitution and Indel Distances to Infer Evolutionary Relationships

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-network 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-gridBase 
Requires:         R-grid 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-ggplot2 

%description
Evolutionary reconstruction based on substitutions and insertion-deletion
(indels) analyses in a distance-based framework as described in
Muñoz-Pajares (2013) <doi:10.1111/2041-210X.12118>.

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
