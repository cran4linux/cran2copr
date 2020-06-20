%global packname  NetworkChange
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          Bayesian Package for Network Changepoint Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggvis 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-network 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggvis 

%description
Network changepoint analysis for undirected network data. The package
implements a hidden Markov network change point model (Park and Sohn
2019). Functions for break number detection using the approximate marginal
likelihood and WAIC are also provided.

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

%files
%{rlibdir}/%{packname}
