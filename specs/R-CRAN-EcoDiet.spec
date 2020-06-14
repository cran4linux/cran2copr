%global packname  EcoDiet
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Estimating a Diet Matrix from Biotracer and Stomach Content Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.10
BuildRequires:    R-stats >= 3.6
BuildRequires:    R-utils >= 3.6
BuildRequires:    R-CRAN-ggplot2 >= 3.2
BuildRequires:    R-CRAN-coda >= 0.19
Requires:         R-CRAN-rjags >= 4.10
Requires:         R-stats >= 3.6
Requires:         R-utils >= 3.6
Requires:         R-CRAN-ggplot2 >= 3.2
Requires:         R-CRAN-coda >= 0.19

%description
Biotracers and stomach content analyses are combined in a Bayesian
hierarchical model to estimate a probabilistic topology matrix (all
trophic link probabilities) and a diet matrix (all diet proportions). The
package relies on the JAGS software and the 'rjags' package to run a
Markov chain Monte Carlo approximation of the different variables.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
