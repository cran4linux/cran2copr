%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BLSM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Latent Space Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.4

%description
Provides a Bayesian latent space model for complex networks, either
weighted or unweighted. Given an observed input graph, the estimates for
the latent coordinates of the nodes are obtained through a Bayesian MCMC
algorithm. The overall likelihood of the graph depends on a fundamental
probability equation, which is defined so that ties are more likely to
exist between nodes whose latent space coordinates are close. The package
is mainly based on the model by Hoff, Raftery and Handcock (2002)
<doi:10.1198/016214502388618906> and contains some extra features (e.g.,
removal of the Procrustean step, weights implemented as coefficients of
the latent distances, 3D plots). The original code related to the above
model was retrieved from
<https://www2.stat.duke.edu/~pdh10/Code/hoff_raftery_handcock_2002_jasa/>.
Users can inspect the MCMC simulation, create and customize insightful
graphical representations or apply clustering techniques.

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
