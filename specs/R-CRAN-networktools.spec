%global packname  networktools
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Tools for Identifying Important Nodes in Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-IsingFit 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-NetworkComparisonTest 
BuildRequires:    R-CRAN-cocor 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-eigenmodel 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-CRAN-wordcloud 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-IsingFit 
Requires:         R-CRAN-reshape2 
Requires:         R-nnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-NetworkComparisonTest 
Requires:         R-CRAN-cocor 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-eigenmodel 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-smacof 
Requires:         R-CRAN-wordcloud 

%description
Includes assorted tools for network analysis. Bridge centrality, impact, &
goldbricker.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
