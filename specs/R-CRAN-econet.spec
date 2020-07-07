%global packname  econet
%global packver   0.1.81
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.81
Release:          3%{?dist}
Summary:          Estimation of Parameter-Dependent Network Centrality Measures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-intergraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-spatstat.utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tnet 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-bbmle 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-intergraph 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-spatstat.utils 
Requires:         R-stats 
Requires:         R-CRAN-tnet 
Requires:         R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 

%description
Provides methods for estimating parameter-dependent network centrality
measures with linear-in-means models. Both non linear least squares and
maximum likelihood estimators are implemented. The methods allow for both
link and node heterogeneity in network effects, endogenous network
formation and the presence of unconnected nodes. The routines also compare
the explanatory power of parameter-dependent network centrality measures
with those of standard measures of network centrality. Benefits and
features of the 'econet' package are illustrated using data from
Battaglini and Patacchini (2018), which examine the determinants of US
campaign contributions when legislators care about the behavior of other
legislators to whom they are socially connected. For additional details,
see the vignette.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
