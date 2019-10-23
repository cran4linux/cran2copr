%global packname  sigora
%global packver   3.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.5
Release:          1%{?dist}
Summary:          Signature Overrepresentation Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-utils 
Requires:         R-stats 

%description
Pathway Analysis is the process of statistically linking observations on
the molecular level to biological processes or pathways on the
systems(i.e. organism, organ, tissue, cell) level. Traditionally, pathway
analysis methods regard pathways as collections of single genes and treat
all genes in a pathway as equally informative. This can lead to
identification of spurious pathways as statistically significant, since
components are often shared amongst pathways. SIGORA seeks to avoid this
pitfall by focusing on genes or gene-pairs that are (as a combination)
specific to a single pathway.  In relying on such pathway gene-pair
signatures (Pathway-GPS), SIGORA inherently uses the status of other genes
in the experimental context to identify the most relevant pathways. The
current version allows for pathway analysis of human and mouse datasets
and contains pre-computed Pathway-GPS data for pathways in the KEGG and
Reactome pathway repositories as well as mechanisms for extracting GPS for
user supplied repositories.

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
%{rlibdir}/%{packname}/INDEX
