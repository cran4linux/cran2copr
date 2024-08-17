%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  poweRbal
%global packver   0.0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Tree Models and the Power of Tree Shape Statistics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-treebalance 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-diversitree 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-treebalance 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-diversitree 

%description
The first goal of this package is to provide a multitude of tree models,
i.e., functions that generate rooted binary trees with a given number of
leaves. Second, the package allows for an easy evaluation and comparison
of tree shape statistics by estimating their power to differentiate
between different tree models. Please note that this R package was
developed alongside the manuscript "Tree balance in phylogenetic models"
by S. J. Kersting, K. Wicke, and M. Fischer (2024)
<doi:10.48550/arXiv.2406.05185>, which provides further background and the
respective mathematical definitions. This project was supported by the
project ArtIGROW, which is a part of the WIR!-Alliance ArtIFARM –
Artificial Intelligence in Farming funded by the German Federal Ministry
of Education and Research (No. 03WIR4805).

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
