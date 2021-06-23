%global __brp_check_rpaths %{nil}
%global packname  dirichletprocess
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Build Dirichlet Process Objects for Bayesian Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 

%description
Perform nonparametric Bayesian analysis using Dirichlet processes without
the need to program the inference algorithms. Utilise included pre-built
models or specify custom models and allow the 'dirichletprocess' package
to handle the Markov chain Monte Carlo sampling. Our Dirichlet process
objects can act as building blocks for a variety of statistical models
including and not limited to: density estimation, clustering and prior
distributions in hierarchical models. See Teh, Y. W. (2011)
<https://www.stats.ox.ac.uk/~teh/research/npbayes/Teh2010a.pdf>, among
many other sources.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
