%global __brp_check_rpaths %{nil}
%global packname  bite
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          2%{?dist}%{?buildtag}
Summary:          Bayesian Integrative Models of Trait Evolution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-vioplot 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-ape 
Requires:         R-MASS 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-vioplot 
Requires:         R-CRAN-xml2 

%description
Contains the JIVE (joint inter and intra-specific model of variance
evolution) model and other Bayesian models aimed at understanding trait
evolution. The goal of the package is to join phylogenetic comparative
models (PCM) that tend to integrate various type of data (individual
observations, environmental data, fossil data) into a hierarchical
Bayesian framework. It contains various PCMs as well as functions to join
those models into a hierarchical Bayesian framework in a flexible and user
friendly way. It contains various Markov chain Monte-Carlo (MCMC)
algorithms, methods for model comparison and many plotting function for
pre- and post-processing data visualization. Finally, this package
integrates functions allowing bridges between 'R' and the 'BEAST2'
implementations of PCMs. Kostikova A, Silvestro D, Pearman PB, Salamin N
(2016) <doi:10.1093/sysbio/syw010>. Gaboriau T, Mendes FK, Joly S,
Silvestro D, Salamin N (in prep).

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

%files
%{rlibdir}/%{packname}
