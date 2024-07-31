%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  avotrex
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Global Dataset of Anthropogenic Extinct Birds and their Traits: Phylogeny Builder

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidytree >= 0.4.6
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-TreeTools 
BuildRequires:    R-utils 
Requires:         R-CRAN-tidytree >= 0.4.6
Requires:         R-CRAN-ape 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-TreeTools 
Requires:         R-utils 

%description
Grafts the extinct bird species from the 'Avotrex' database (Sayol et al.,
in review) on to the 'BirdTree' phylogenies <https://birdtree.org>, using
a set of different commands.

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
