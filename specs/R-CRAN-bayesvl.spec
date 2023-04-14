%global __brp_check_rpaths %{nil}
%global packname  bayesvl
%global packver   0.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.5
Release:          3%{?dist}%{?buildtag}
Summary:          Visually Learning the Graphical Structure of Bayesian Networksand Performing MCMC with 'Stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstan >= 2.10.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-StanHeaders >= 2.18.0
Requires:         R-CRAN-rstan >= 2.10.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 

%description
Provides users with its associated functions for pedagogical purposes in
visually learning Bayesian networks and Markov chain Monte Carlo (MCMC)
computations. It enables users to: a) Create and examine the (starting)
graphical structure of Bayesian networks; b) Create random Bayesian
networks using a dataset with customized constraints; c) Generate 'Stan'
code for structures of Bayesian networks for sampling the data and
learning parameters; d) Plot the network graphs; e) Perform Markov chain
Monte Carlo computations and produce graphs for posteriors checks. The
package refers to one reference item, which describes the methods and
algorithms: Vuong, Quan-Hoang and La, Viet-Phuong (2019)
<doi:10.31219/osf.io/w5dx6> The 'bayesvl' R package. Open Science
Framework (May 18).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
