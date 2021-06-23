%global __brp_check_rpaths %{nil}
%global packname  bipartiteD3
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Bipartite Graphs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.4
BuildRequires:    R-CRAN-stringr >= 1.3
BuildRequires:    R-CRAN-RColorBrewer >= 1.1
BuildRequires:    R-CRAN-tidyr >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-downloader >= 0.4
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-r2d3 >= 0.2.2
Requires:         R-CRAN-tibble >= 1.4
Requires:         R-CRAN-stringr >= 1.3
Requires:         R-CRAN-RColorBrewer >= 1.1
Requires:         R-CRAN-tidyr >= 0.8
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-downloader >= 0.4
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-r2d3 >= 0.2.2

%description
Generates interactive bipartite graphs using the D3 library. Designed for
use with the 'bipartite' analysis package. Sources open source 'vis-js'
library (<http://visjs.org/>). Adapted from examples at
<https://bl.ocks.org/NPashaP> (released under GPL-3).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
