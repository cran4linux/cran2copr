%global packname  gemtc
%global packver   0.8-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}
Summary:          Network Meta-Analysis Using Bayesian Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rjags >= 4.0
BuildRequires:    R-CRAN-meta >= 2.1
BuildRequires:    R-CRAN-plyr >= 1.8
BuildRequires:    R-CRAN-igraph >= 1.0
BuildRequires:    R-CRAN-coda >= 0.13
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-Rglpk 
Requires:         R-CRAN-rjags >= 4.0
Requires:         R-CRAN-meta >= 2.1
Requires:         R-CRAN-plyr >= 1.8
Requires:         R-CRAN-igraph >= 1.0
Requires:         R-CRAN-coda >= 0.13
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-Rglpk 

%description
Network meta-analyses (mixed treatment comparisons) in the Bayesian
framework using JAGS. Includes methods to assess heterogeneity and
inconsistency, and a number of standard visualizations.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/gemtc.armeffect.likelihood.txt
%doc %{rlibdir}/%{packname}/gemtc.fixedeffect.txt
%doc %{rlibdir}/%{packname}/gemtc.likelihood.binom.power.txt
%doc %{rlibdir}/%{packname}/gemtc.likelihood.binom.txt
%doc %{rlibdir}/%{packname}/gemtc.likelihood.normal.power.txt
%doc %{rlibdir}/%{packname}/gemtc.likelihood.normal.txt
%doc %{rlibdir}/%{packname}/gemtc.likelihood.poisson.power.txt
%doc %{rlibdir}/%{packname}/gemtc.likelihood.poisson.txt
%doc %{rlibdir}/%{packname}/gemtc.model.template.txt
%doc %{rlibdir}/%{packname}/gemtc.model.use.template.txt
%doc %{rlibdir}/%{packname}/gemtc.randomeffects.txt
%doc %{rlibdir}/%{packname}/gemtc.releffect.likelihood.power.r2.txt
%doc %{rlibdir}/%{packname}/gemtc.releffect.likelihood.power.rm.txt
%doc %{rlibdir}/%{packname}/gemtc.releffect.likelihood.r2.txt
%doc %{rlibdir}/%{packname}/gemtc.releffect.likelihood.rm.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
