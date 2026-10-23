%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rTARDIS
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Terrains and Routes Directed in Spacetime

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-cppRouting 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-h3jsr 
BuildRequires:    R-CRAN-h3r 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-palaeoverse 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-rlemon 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-cppRouting 
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-h3jsr 
Requires:         R-CRAN-h3r 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-palaeoverse 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-rlemon 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-terra 

%description
Implements classes and methods for constructing and analysing graph
representations of complex geographic spaces at local to global scales,
particularly where accessible spaces are discontinuously distributed but
retain connectivity (e.g., island systems where isolation is prevalent but
not necessarily absolute), and where that distribution also changes
through time (e.g., habitat patch fragmentation or plate tectonic drift).
The package (originally named TARDIS) was first described and published
in: Flannery-Sutherland, J., Elsler, A., Farnsworth, A., Lunt, D., Benton,
M. (2025) <doi:10.1038/s41559-025-02739-y>.

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
