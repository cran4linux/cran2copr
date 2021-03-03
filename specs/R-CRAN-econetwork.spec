%global packname  econetwork
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Ecological Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rdiversity 
BuildRequires:    R-CRAN-Matrix.utils 
BuildRequires:    R-CRAN-blockmodels 
BuildRequires:    R-CRAN-bipartite 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rdiversity 
Requires:         R-CRAN-Matrix.utils 
Requires:         R-CRAN-blockmodels 
Requires:         R-CRAN-bipartite 
Requires:         R-CRAN-Rcpp 

%description
A collection of advanced tools, methods and models specifically designed
for analyzing different types of ecological networks - especially
antagonistic (food webs, host-parasite), mutualistic (plant-pollinator,
plant-fungus, etc) and competitive networks, as well as their variability
in time and space. Statistical models are developed to describe and
understand the mechanisms that determine species interactions, and to
decipher the organization of these ecological networks (Ohlmann et al.
(2019) <doi:10.1111/ele.13221>, Gonzalez et al. (2020)
<doi:10.1101/2020.04.02.021691>, Miele et al. (2021) submitted).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
