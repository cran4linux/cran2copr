%global packname  tapnet
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Trait Matching and Abundance for Predicting Bipartite Networks

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-bipartite 
BuildRequires:    R-CRAN-MPSEM 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-bipartite 
Requires:         R-CRAN-MPSEM 
Requires:         R-CRAN-phytools 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vegan 

%description
Functions to produce, fit and predict from bipartite networks with
abundance, trait and phylogenetic information. Its methods are described
in detail in Benadi, G., Dormann, C.F., Fruend, J., Stephan, R. & Vazquez,
D.P. (2021) Quantitative prediction of interactions in bipartite networks
based on traits, abundances, and phylogeny. The American Naturalist, in
press.

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
