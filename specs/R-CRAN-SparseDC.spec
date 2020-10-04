%global packname  SparseDC
%global packver   0.1.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.17
Release:          3%{?dist}%{?buildtag}
Summary:          Implementation of SparseDC Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implements the algorithm described in Barron, M., Zhang, S. and Li, J.
2017, "A sparse differential clustering algorithm for tracing cell type
changes via single-cell RNA-sequencing data", Nucleic Acids Research,
gkx1113, <doi:10.1093/nar/gkx1113>. This algorithm clusters samples from
two different populations, links the clusters across the conditions and
identifies marker genes for these changes. The package was designed for
scRNA-Seq data but is also applicable to many other data types, just
replace cells with samples and genes with variables. The package also
contains functions for estimating the parameters for SparseDC as outlined
in the paper. We recommend that users further select their marker genes
using the magnitude of the cluster centers.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
