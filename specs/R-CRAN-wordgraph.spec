%global packname  wordgraph
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Graph Functionality of Free Associated Words

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 

%description
Functions that help less experienced R users to make graph analysis for
free associated words, or more generally for repeated nominal data for
which a undirected graph analysis is meaningful. By corresponding to each
word its centrality, it is possible to apply standard quantitative
analysis methods in order to associate word selection with other
variables. The functions are implemented with the aid of the 'tibble',
'tidygraph', 'ggraph' and 'ggplot2' packages. Supported centrality
functions are centrality_alpha(), centrality_authority(),
centrality_betweenness(), centrality_closeness(), centrality_pagerank(),
centrality_eigen(). A data set is included.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
