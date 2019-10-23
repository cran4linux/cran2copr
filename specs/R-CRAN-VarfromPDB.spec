%global packname  VarfromPDB
%global packver   2.2.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.10
Release:          1%{?dist}
Summary:          Disease-Gene-Variant Relations Mining from the Public Databasesand Literature

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-XML2R 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-RISmed 
BuildRequires:    R-utils 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-XML2R 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-RISmed 
Requires:         R-utils 

%description
Captures and compiles the genes and variants related to a disease, a
phenotype or a clinical feature from the public databases including HPO
(Human Phenotype Ontology,
<http://human-phenotype-ontology.github.io/about.html>), Orphanet
<http://www.orpha.net/consor/cgi-bin/index.php>, OMIM (Online Mendelian
Inheritance in Man, <http://www.omim.org>), ClinVar
<http://www.ncbi.nlm.nih.gov/clinvar>, and UniProt (Universal Protein
Resource, <http://www.uniprot.org>) and PubMed abstracts. HPO provides a
standardized vocabulary of phenotypic abnormalities encountered in human
disease. HPO currently contains approximately 11,000 terms and over
115,000 annotations to hereditary diseases. Orphanet is the reference
portal for information on rare diseases and orphan drugs, whose aim is to
help improve the diagnosis, care and treatment of patients with rare
diseases. OMIM is a continuously updated catalog of human genes and
genetic disorders and traits, with particular focus on the molecular
relationship between genetic variation and phenotypic expression. ClinVar
is a freely accessible, public archive of reports of the relationships
among human variations and phenotypes, with supporting evidence. UniProt
focuses on amino acid altering variants imported from Ensembl Variation
databases. For Homo sapiens, the variants including human polymorphisms
and disease mutations in the UniProt are manually curated from
UniProtKB/Swiss-Prot. Additionally, PubMed provides the primary and latest
source of the information. Text mining was employed to capture the
information from PubMed abstracts.

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
