%global packname  corto
%global packver   0.99.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.10
Release:          1%{?dist}
Summary:          Inference of Gene Regulatory Networks

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-knitr 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 
Requires:         R-utils 

%description
We present 'corto' (Correlation Tool), a simple package to infer gene
regulatory networks using DPI (Data Processing Inequality) and
bootstrapping to recover edges. An initial step is performed to calculate
all significant edges between a list of source nodes (centroids) and
target genes. Then all triplets containing two centroids and one target
are tested in a DPI step which removes edges. A bootstrapping process then
calculates the robustness of the network, eventually re-adding edges
previously removed by DPI. The package implements a similar pipeline as
ARACNe-AP (Algorithm for the Reconstruction of Accurate Cellular Networks
with Adaptive Partitioning) by Giorgi (2016)
<doi:10.1093/bioinformatics/btw216>) with optimizations to run outside a
computing cluster (most notably correlation to infer feature dependencies
instead of Mutual Information).

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
