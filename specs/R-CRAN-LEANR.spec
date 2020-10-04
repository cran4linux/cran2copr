%global packname  LEANR
%global packver   1.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.9
Release:          3%{?dist}%{?buildtag}
Summary:          Finds "Local Subnetworks" Within an Interaction Network whichShow Enrichment for Differentially Expressed Genes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach >= 1.4.2
BuildRequires:    R-CRAN-igraph >= 0.7.1
Requires:         R-CRAN-foreach >= 1.4.2
Requires:         R-CRAN-igraph >= 0.7.1

%description
Implements the method described in "Network-based analysis of omics data:
The LEAN method" [Gwinner Boulday (2016)
<DOI:10.1093/bioinformatics/btw676>] Given a protein interaction network
and a list of p-values describing a measure of interest (as e.g.
differential gene expression) this method computes an enrichment p-value
for the protein neighborhood of each gene and compares it to a background
distribution of randomly drawn p-values. The resulting scores are
corrected for multiple testing and significant hits are returned in
tabular format.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
