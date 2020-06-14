%global packname  genotypeR
%global packver   0.0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.8
Release:          2%{?dist}
Summary:          SNP Genotype Marker Design and Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         vcftools
Requires:         perl
Requires:         gawk
Requires:         bash
BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-colorspace 

%description
We implement a common genotyping workflow with a standardized software
interface. 'genotypeR' designs genotyping markers from vcf files, outputs
markers for multiplexing suitability on various platforms (Sequenom and
Illumina GoldenGate), and provides various QA/QC and analysis functions.
We developed this package to analyze data in Stevison LS, SA Sefick, CA
Rushton, and RM Graze. 2017. Invited Review: Recombination rate
plasticity: revealing mechanisms by design. Philosophical Transactions
Royal Society London B Biol Sci 372:1-14. <DOI:10.1098/rstb.2016.0459>,
and have published it here Sefick, S.A., M.A. Castronova, and L.S.
Stevison. 2017. GENOTYPER: An integrated R packages for single nuleotide
polymorphism genotype marker design and data analysis. Methods in Ecology
and Evolution 9: 1318-1323. <DOI: 10.1111/2041-210X.12965>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/get_SequenomMarkers_and_remove_git.sh
%doc %{rlibdir}/%{packname}/SequenomMarkers
%doc %{rlibdir}/%{packname}/SequenomMarkers_v2
%{rlibdir}/%{packname}/INDEX
