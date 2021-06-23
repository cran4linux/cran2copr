%global __brp_check_rpaths %{nil}
%global packname  aptg
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Phylogenetic Tree Generator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-brranching 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-brranching 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-xml2 

%description
Generates phylogenetic trees and distance matrices ('brranching',
<https://CRAN.R-project.org/package=brranching>) from a list of species
name or from a taxon down to whatever lower taxon ('taxize',
<https://github.com/ropensci/taxize>). It can do so based on two reference
super trees: mammals (Bininda-Emonds et al., 2007;
<doi:10.1038/nature05634>) and angiosperms (Zanne et al., 2014;
<doi:10.1038/nature12872>).

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
