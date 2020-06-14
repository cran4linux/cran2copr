%global packname  MHCtools
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          Analysis of MHC Data in Non-Model Species

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlist >= 0.4.6.1
BuildRequires:    R-utils 
Requires:         R-CRAN-rlist >= 0.4.6.1
Requires:         R-utils 

%description
Ten tools for analysis of major histocompatibility complex (MHC) data in
non- model species. The functions are tailored for amplicon data sets that
have been filtered using the 'dada2' method (for more information visit
<https://benjjneb.github.io/dada2>), but even other data sets can be
analyzed, if the data tables are formatted according to the description in
each function. The ReplMatch() function matches replicates in data sets in
order to evaluate genotyping success. The GetReplTable() and
GetReplStats() functions perform such an evaluation. The HpltFind()
function infers putative haplotypes from families in the data set. The
GetHpltTable() and GetHpltStats() functions evaluate the accuracy of the
haplotype inference. The PapaDiv() function compares parent pairs in the
data set and calculate their joint MHC diversity, taking into account
sequence variants that occur in both parents. The CalcPdist() function
calculates the p-distances from pairwise comparisons of all sequences in a
data set, and mean p-distances of all pairwise comparisons within each
sample in a data set. The function includes the options to specify which
codons to compare and to calculate amino acid p-distances. The CreateFas()
function creates a fasta file with all the sequences in the data set. The
CreateSamplesFas() function creates a fasta file for each sample in the
data set.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
