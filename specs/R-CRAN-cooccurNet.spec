%global packname  cooccurNet
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Co-Occurrence Network

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-bigmemory 
Requires:         R-Matrix 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-doParallel 

%description
Read and preprocess fasta format data, and construct the co-occurrence
network for downstream analyses. This R package is to construct the
co-occurrence network with the algorithm developed by Du (2008)
<DOI:10.1101/gr.6969007>. It could be used to transform the data with
high-dimension, such as DNA or protein sequence, into co-occurrence
networks. Co-occurrence network could not only capture the co-variation
pattern between variables, such as the positions in DNA or protein
sequences, but also reflect the relationship between samples. Although it
is originally used in DNA and protein sequences, it could be also used to
other kinds of data, such as RNA, SNP, etc.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
