%global packname  econet
%global packver   0.1.91
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.91
Release:          1%{?dist}%{?buildtag}
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
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-bbmle 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-intergraph 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-spatstat.utils 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-foreach 

%description
Provides methods for estimating parameter-dependent network centrality
measures with linear-in-means models. Both non linear least squares and
maximum likelihood estimators are implemented. The methods allow for both
link and node heterogeneity in network effects, endogenous network
formation and the presence of unconnected nodes. The routines also compare
the explanatory power of parameter-dependent network centrality measures
with those of standard measures of network centrality. Benefits and
features of the 'econet' package are illustrated using data from
Battaglini and Patacchini (2018) and Battaglini, Patacchini, and Leone
Sciabolazza (2020). For additional details, see the vignette.

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
