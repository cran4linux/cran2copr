%global packname  pivmet
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pivotal Methods for Bayesian Relabelling and k-Means Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
Requires:         pandoc-citeproc
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-bayesmix 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-runjags 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-bayesmix 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-rstantools

%description
Collection of pivotal algorithms for: relabelling the MCMC chains in order
to undo the label switching problem in Bayesian mixture models, as
proposed in Egidi, Pappadà, Pauli and Torelli
(2018a)<doi:10.1007/s11222-017-9774-2>; initializing the centers of the
classical k-means algorithm in order to obtain a better clustering
solution. For further details see Egidi, Pappadà, Pauli and Torelli
(2018b)<ISBN:9788891910233>.

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
