%global packname  betapart
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Partitioning Beta Diversity into Turnover and Nestedness Components

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-rcdd 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-itertools 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-rcdd 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-itertools 

%description
Functions to compute pair-wise dissimilarities (distance matrices) and
multiple-site dissimilarities, separating the turnover and
nestedness-resultant components of taxonomic (incidence and abundance
based), functional and phylogenetic beta diversity.

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
