%global packname  bibliometrix
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}
Summary:          An R-Tool for Comprehensive Science Mapping Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dimensionsR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-pubmedR 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-rscopus 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-dimensionsR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-igraph 
Requires:         R-Matrix 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-pubmedR 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-rscopus 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 

%description
Tool for quantitative research in scientometrics and bibliometrics. It
provides various routines for importing bibliographic data from 'SCOPUS'
(<http://scopus.com>), 'Clarivate Analytics Web of Science'
(<http://www.webofknowledge.com/>), 'Digital Science Dimensions'
(<https://www.dimensions.ai/>), 'Cochrane Library'
(<http://www.cochranelibrary.com/>) and 'PubMed'
(<https://www.ncbi.nlm.nih.gov/pubmed/>) databases, performing
bibliometric analysis and building networks for co-citation, coupling,
scientific collaboration and co-word analysis.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/biblioshiny
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/logo
%{rlibdir}/%{packname}/INDEX
