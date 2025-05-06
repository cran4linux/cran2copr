%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  binspp
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference for Neyman-Scott Point Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-spatstat.model 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-spatstat.model 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-fields 

%description
The Bayesian MCMC estimation of parameters for Thomas-type cluster point
process with various inhomogeneities. It allows for inhomogeneity in (i)
distribution of parent points, (ii) mean number of points in a cluster,
(iii) cluster spread. The package also allows for the Bayesian MCMC
algorithm for the homogeneous generalized Thomas process. The cluster size
is allowed to have a variance that is greater or less than the expected
value (cluster sizes are over or under dispersed). Details are described
in Dvořák, Remeš, Beránek & Mrkvička (2022) <arXiv:
10.48550/arXiv.2205.07946>.

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
