%global packname  hadron
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          2%{?dist}
Summary:          Analysis Framework for Monte Carlo Simulation Data in Physics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-abind 
Requires:         R-boot 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-stringr 

%description
Toolkit to perform statistical analyses of correlation functions generated
from Lattice Monte Carlo simulations. In particular, a class 'cf' for
correlation functions and methods to analyse those are defined. This
includes (blocked) bootstrap (based on the 'boot' package) and jackknife,
but also an automatic determination of integrated autocorrelation times.
'hadron' also provides a very general function bootstrap.nlsfit() to
bootstrap a non-linear least squares fit. More specific functions are
provided to extract hadronic quantities from Lattice Quantum
Chromodynamics simulations, a particular Monte Carlo simulation,(see e.g.
European Twisted Mass Collaboration, P. Boucaud et al. (2008)
<doi:10.1016/j.cpc.2008.06.013>). Here, to determine energy eigenvalues of
hadronic states, specific fitting routines and in particular the
generalised eigenvalue method (see e.g. B. Blossier et al. (2009)
<doi:10.1088/1126-6708/2009/04/094> and M. Fischer et al. (2020)
<https://inspirehep.net/literature/1792113>) are implemented. In addition,
input/output and plotting routines are available.

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
