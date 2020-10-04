%global packname  MiRSEA
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          'MicroRNA' Set Enrichment Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch

%description
The tools for 'MicroRNA Set Enrichment Analysis' can identify risk
pathways(or prior gene sets) regulated by microRNA set in the context of
microRNA expression data. (1) This package constructs a correlation
profile of microRNA and pathways by the hypergeometric statistic test. The
gene sets of pathways derived from the three public databases (Kyoto
Encyclopedia of Genes and Genomes ('KEGG'); 'Reactome'; 'Biocarta') and
the target gene sets of microRNA are provided by four
databases('TarBaseV6.0'; 'mir2Disease'; 'miRecords'; 'miRTarBase';). (2)
This package can quantify the change of correlation between microRNA for
each pathway(or prior gene set) based on a microRNA expression data with
cases and controls. (3) This package uses the weighted Kolmogorov-Smirnov
statistic to calculate an enrichment score (ES) of a microRNA set that
co-regulate to a pathway , which reflects the degree to which a given
pathway is associated with the specific phenotype. (4) This package can
provide the visualization of the results.

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
%{rlibdir}/%{packname}/localdata
%{rlibdir}/%{packname}/INDEX
