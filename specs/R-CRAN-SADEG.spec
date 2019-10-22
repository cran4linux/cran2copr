%global packname  SADEG
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Stability Analysis in Differentially Expressed Genes

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch

%description
We analyzed the nucleotide composition of genes with a special emphasis on
stability of DNA sequences. Besides, in a variety of different organisms
unequal use of synonymous codons, or codon usage bias, occurs which also
show variation among genes in the same genome. Seemingly, codon usage bias
is affected by both selective constraints and mutation bias which allows
and enables us to examine and detect changes in these two evolutionary
forces between genomes or along one genome. Therefore, we determined the
codon adaptation index (CAI), effective number of codons (ENC) and codon
usage analysis with calculation of the relative synonymous codon usage
(RSCU), and subsequently predicted the translation efficiency and accuracy
through GC-rich codon usages. Furthermore, we estimated the relative
stability of the DNA sequence following calculation of the average free
energy (Delta G) and Dimer base-stacking energy level.

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
%{rlibdir}/%{packname}/INDEX
