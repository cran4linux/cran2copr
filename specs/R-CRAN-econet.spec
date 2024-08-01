%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  econet
%global packver   1.0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.1
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
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
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
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
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
Sciabolazza (2020). For additional details, see the vignette
<doi:10.18637/jss.v102.i08>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
