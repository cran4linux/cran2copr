%global __brp_check_rpaths %{nil}
%global packname  BSBT
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Bayesian Spatial Bradley--Terry Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-expm 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-utils 
Requires:         R-CRAN-expm 

%description
An implementation of the Bayesian Spatial Bradley--Terry (BSBT) model. It
can be used to investigate data sets where judges compared different
spatial areas. It constructs a network to describe how the areas are
connected, and then places a correlated prior distribution on the quality
parameter for each area, based on the network. The package includes MCMC
algorithms to estimate the quality parameters. The methodology is
published in Seymour et. al. (2020) <arXiv:2010.14128>.

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
