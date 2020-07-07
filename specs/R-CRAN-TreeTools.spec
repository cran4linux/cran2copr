%global packname  TreeTools
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Create, Modify and Analyse Phylogenetic Trees

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-phangorn >= 2.2.1
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-phangorn >= 2.2.1
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-R.cache 

%description
Efficient implementations of functions for the creation, modification and
analysis of phylogenetic trees. Applications include: generation of trees
with specified shapes; rooting of trees and extraction of subtrees;
calculation and depiction of node support; calculation of
ancestor-descendant relationships; import and export of trees from Newick,
Nexus (Maddison et al. 1997) <doi:10.1093/sysbio/46.4.590>, and TNT
<http://www.lillo.org.ar/phylogeny/tnt/> formats; and analysis of
partitions and cladistic information.

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
%doc %{rlibdir}/%{packname}/apa-old-doi-prefix.csl
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
