%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phyloregion
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Biogeographic Regionalization and Macroecology

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-betapart 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-clustMixType 
BuildRequires:    R-CRAN-maptpx 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-predicts 
BuildRequires:    R-CRAN-smoothr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-betapart 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-clustMixType 
Requires:         R-CRAN-maptpx 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-predicts 
Requires:         R-CRAN-smoothr 

%description
Computational infrastructure for biogeography, community ecology, and
biodiversity conservation (Daru et al. 2020)
<doi:10.1111/2041-210X.13478>. It is based on the methods described in
Daru et al. (2020) <doi:10.1038/s41467-020-15921-6>. The original
conceptual work is described in Daru et al. (2017)
<doi:10.1016/j.tree.2017.08.013> on patterns and processes of
biogeographical regionalization. Additionally, the package contains fast
and efficient functions to compute more standard conservation measures
such as phylogenetic diversity, phylogenetic endemism, evolutionary
distinctiveness and global endangerment, as well as compositional turnover
(e.g., beta diversity).

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
