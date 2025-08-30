%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BDgraph
%global packver   2.74
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.74
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Structure Learning in Graphical Models using Birth-Death MCMC

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 

%description
Advanced statistical tools for Bayesian structure learning in undirected
graphical models, accommodating continuous, ordinal, discrete, count, and
mixed data. It integrates recent advancements in Bayesian graphical models
as presented in the literature, including the works of Mohammadi and Wit
(2015) <doi:10.1214/14-BA889>, Mohammadi et al. (2021)
<doi:10.1080/01621459.2021.1996377>, Dobra and Mohammadi (2018)
<doi:10.1214/18-AOAS1164>, and Mohammadi et al. (2023)
<doi:10.48550/arXiv.2307.00127>.

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
