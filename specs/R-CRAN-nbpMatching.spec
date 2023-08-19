%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nbpMatching
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Optimal Non-Bipartite Matching

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-MASS 
Requires:         R-utils 

%description
Perform non-bipartite matching and matched randomization. A "bipartite"
matching utilizes two separate groups, e.g. smokers being matched to
nonsmokers or cases being matched to controls. A "non-bipartite" matching
creates mates from one big group, e.g. 100 hospitals being randomized for
a two-arm cluster randomized trial or 5000 children who have been exposed
to various levels of secondhand smoke and are being paired to form a
greater exposure vs. lesser exposure comparison. At the core of a
non-bipartite matching is a N x N distance matrix for N potential mates.
The distance between two units expresses a measure of similarity or
quality as mates (the lower the better). The 'gendistance()' and
'distancematrix()' functions assist in creating this. The 'nonbimatch()'
function creates the matching that minimizes the total sum of distances
between mates; hence, it is referred to as an "optimal" matching. The
'assign.grp()' function aids in performing a matched randomization. Note
bipartite matching can be performed using the prevent option in
'gendistance()'.

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
