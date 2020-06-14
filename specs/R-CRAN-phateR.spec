%global packname  phateR
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          2%{?dist}
Summary:          PHATE - Potential of Heat-Diffusion for Affinity-BasedTransition Embedding

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.8
BuildRequires:    R-Matrix >= 1.2.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-reticulate >= 1.8
Requires:         R-Matrix >= 1.2.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-memoise 

%description
PHATE is a tool for visualizing high dimensional single-cell data with
natural progressions or trajectories. PHATE uses a novel conceptual
framework for learning and visualizing the manifold inherent to biological
systems in which smooth transitions mark the progressions of cells from
one state to another. To see how PHATE can be applied to single-cell
RNA-seq datasets from hematopoietic stem cells, human embryonic stem
cells, and bone marrow samples, check out our publication in Nature
Biotechnology at <doi:10.1038/s41587-019-0336-3>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
