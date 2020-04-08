%global packname  btergm
%global packver   1.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.7
Release:          1%{?dist}
Summary:          Temporal Exponential Random Graph Models by BootstrappedPseudolikelihood

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-statnet.common >= 4.2.0
BuildRequires:    R-CRAN-ergm >= 3.10.0
BuildRequires:    R-CRAN-sna >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-xergm.common >= 1.7.7
BuildRequires:    R-boot >= 1.3.17
BuildRequires:    R-Matrix >= 1.2.2
BuildRequires:    R-CRAN-network >= 1.13.0
BuildRequires:    R-CRAN-ROCR >= 1.0.7
BuildRequires:    R-CRAN-RSiena >= 1.0.12.232
BuildRequires:    R-CRAN-igraph >= 0.7.1
BuildRequires:    R-CRAN-speedglm >= 0.3.1
BuildRequires:    R-CRAN-coda >= 0.18.1
BuildRequires:    R-stats4 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-statnet.common >= 4.2.0
Requires:         R-CRAN-ergm >= 3.10.0
Requires:         R-CRAN-sna >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-xergm.common >= 1.7.7
Requires:         R-boot >= 1.3.17
Requires:         R-Matrix >= 1.2.2
Requires:         R-CRAN-network >= 1.13.0
Requires:         R-CRAN-ROCR >= 1.0.7
Requires:         R-CRAN-RSiena >= 1.0.12.232
Requires:         R-CRAN-igraph >= 0.7.1
Requires:         R-CRAN-speedglm >= 0.3.1
Requires:         R-CRAN-coda >= 0.18.1
Requires:         R-stats4 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-stats 

%description
Temporal Exponential Random Graph Models (TERGM) estimated by maximum
pseudolikelihood with bootstrapped confidence intervals or Markov Chain
Monte Carlo maximum likelihood. Goodness of fit assessment for ERGMs,
TERGMs, and SAOMs. Micro-level interpretation of ERGMs and TERGMs.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
