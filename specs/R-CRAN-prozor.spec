%global packname  prozor
%global packver   0.2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.11
Release:          3%{?dist}
Summary:          Minimal Protein Set Explaining Peptide Spectrum Matches

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-AhoCorasickTrie 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-AhoCorasickTrie 
Requires:         R-Matrix 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 

%description
Determine minimal protein set explaining peptide spectrum matches. Utility
functions for creating fasta amino acid databases with decoys and
contaminants. Peptide false discovery rate estimation for target decoy
search results on psm, precursor, peptide and protein level.

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
%doc %{rlibdir}/%{packname}/creatingDBs
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/p1000_db1_example
%{rlibdir}/%{packname}/INDEX
