%global packname  clustree
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          2%{?dist}
Summary:          Visualise Clusterings at Different Resolutions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-viridis 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-ggrepel 

%description
Deciding what resolution to use can be a difficult question when
approaching a clustering analysis. One way to approach this problem is to
look at how samples move as the number of clusters increases. This package
allows you to produce clustering trees, a visualisation for interrogating
clusterings as resolution increases.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
