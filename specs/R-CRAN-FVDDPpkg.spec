%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FVDDPpkg
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Implement Fleming-Viot-Dependent Dirichlet Processes

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 

%description
A Bayesian Nonparametric model for the study of time-evolving frequencies,
which has become renowned in the study of population genetics. The model
consists of a Hidden Markov Model (HMM) in which the latent signal is a
distribution-valued stochastic process that takes the form of a finite
mixture of Dirichlet Processes, indexed by vectors that count how many
times each value is observed in the population. The package implements
methodologies presented in Ascolani, Lijoi and Ruggiero (2021)
<doi:10.1214/20-BA1206> and Ascolani, Lijoi and Ruggiero (2023)
<doi:10.3150/22-BEJ1504> that make it possible to study the process at the
time of data collection or to predict its evolution in future or in the
past.

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
