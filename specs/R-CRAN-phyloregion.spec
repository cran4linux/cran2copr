%global packname  phyloregion
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Biogeographic Regionalization and Spatial Conservation

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
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phangorn 
Requires:         R-Matrix 
Requires:         R-CRAN-betapart 
Requires:         R-CRAN-fastmatch 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-colorspace 
Requires:         R-cluster 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-igraph 

%description
Computational infrastructure for biogeography, community ecology, and
biodiversity conservation (Daru et al. 2020)
<doi:10.1101/2020.02.12.945691>. It is based on the conceptual work in
Daru et al.(2017) <doi:10.1016/j.tree.2017.08.013> on patterns and
processes of biogeographical regionalization. Additionally, the package
contains fast and efficient functions to compute more standard
conservation measures such as phylogenetic diversity, phylogenetic
endemism, evolutionary distinctiveness and global endangerment, as well as
compositional turnover (e.g., beta diversity).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NGAplants
%doc %{rlibdir}/%{packname}/nigeria
%doc %{rlibdir}/%{packname}/phyloregion_sticker.png
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
