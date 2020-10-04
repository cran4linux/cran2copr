%global packname  phyloregion
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Biogeographic Regionalization and Macroecology

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-betapart 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phangorn 
Requires:         R-Matrix 
Requires:         R-CRAN-betapart 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 

%description
Computational infrastructure for biogeography, community ecology, and
biodiversity conservation (Daru et al. 2020)
<doi:10.1101/2020.02.12.945691>. It is based on the methods described in
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
