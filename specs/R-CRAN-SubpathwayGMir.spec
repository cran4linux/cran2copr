%global packname  SubpathwayGMir
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Identify Metabolic Subpathways Mediated by MicroRNAs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-igraph 

%description
Routines for identifying metabolic subpathways mediated by microRNAs
(miRNAs) through topologically locating miRNAs and genes within
reconstructed Kyoto Encyclopedia of Genes and Genomes (KEGG) metabolic
pathway graphs embedded by miRNAs. (1) This package can obtain the
reconstructed KEGG metabolic pathway graphs with genes and miRNAs as
nodes, through converting KEGG metabolic pathways to graphs with genes as
nodes and compounds as edges, and then integrating miRNA-target
interactions verified by low-throughput experiments from four databases
(TarBase, miRecords, mirTarBase and miR2Disease) into converted pathway
graphs. (2) This package can locate metabolic subpathways mediated by
miRNAs by topologically analyzing the "lenient distance" of miRNAs and
genes within reconstructed KEGG metabolic pathway graphs.(3) This package
can identify significantly enriched miRNA-mediated metabolic subpathways
based on located subpathways by hypergenomic test. (4) This package can
support six species for metabolic subpathway identification, such as
caenorhabditis elegans, drosophila melanogaster, danio rerio, homo
sapiens, mus musculus and rattus norvegicus, and user only need to update
interested organism-specific environment variables.

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
