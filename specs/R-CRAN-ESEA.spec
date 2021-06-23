%global __brp_check_rpaths %{nil}
%global packname  ESEA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          ESEA: Discovering the Dysregulated Pathways based on Edge SetEnrichment Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-parmigene 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-parmigene 

%description
The package can identify the dysregulated canonical pathways by
investigating the changes of biological relationships of pathways in the
context of gene expression data. (1) The ESEA package constructs a
background set of edges by extracting pathway structure (e.g. interaction,
regulation, modification, and binding etc.) from the seven public
databases (KEGG; Reactome; Biocarta; NCI; SPIKE; HumanCyc; Panther) and
the edge sets of pathways for each of the above databases. (2) The ESEA
package can can quantify the change of correlation between genes for each
edge based on gene expression data with cases and controls. (3) The ESEA
package uses the weighted Kolmogorov-Smirnov statistic to calculate an
edge enrichment score (EES), which reflects the degree to which a given
pathway is associated the specific phenotype. (4) The ESEA package can
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
%{rlibdir}/%{packname}/INDEX
