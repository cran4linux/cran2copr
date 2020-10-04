%global packname  wTO
%global packver   1.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.3
Release:          3%{?dist}%{?buildtag}
Summary:          Computing Weighted Topological Overlaps (wTO) & Consensus wTONetwork

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-som 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 
Requires:         R-parallel 
Requires:         R-CRAN-som 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-shiny 

%description
Computes the Weighted Topological Overlap with positive and negative signs
(wTO) networks given a data frame containing the mRNA count/ expression/
abundance per sample, and a vector containing the interested nodes of
interaction (a subset of the elements of the full data frame). It also
computes the cut-off threshold or p-value based on the individuals
bootstrap or the values reshuffle per individual. It also allows the
construction of a consensus network, based on multiple wTO networks. The
package includes a visualization tool for the networks.  More about the
methodology can be found at <arXiv:1711.04702>.

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
%{rlibdir}/%{packname}/INDEX
