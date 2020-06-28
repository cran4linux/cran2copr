%global packname  corto
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Inference of Gene Regulatory Networks

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-knitr 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 
Requires:         R-utils 

%description
We present 'corto' (Correlation Tool), a simple package to infer gene
regulatory networks and visualize master regulators from gene expression
data using DPI (Data Processing Inequality) and bootstrapping to recover
edges. An initial step is performed to calculate all significant edges
between a list of source nodes (centroids) and target genes. Then all
triplets containing two centroids and one target are tested in a DPI step
which removes edges. A bootstrapping process then calculates the
robustness of the network, eventually re-adding edges previously removed
by DPI. The algorithm has been optimized to run outside a computing
cluster, using a fast correlation implementation. The package finally
provides functions to calculate network enrichment analysis from RNA-Seq
and ATAC-Seq signatures as described in the article by Giorgi lab (2020)
<doi:10.1093/bioinformatics/btaa223>.

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
