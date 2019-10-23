%global packname  jarbes
%global packver   1.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}
Summary:          Just a Rather Bayesian Evidence Synthesis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 3.4
BuildRequires:    R-CRAN-R2jags >= 0.04.03
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggExtra 
BuildRequires:    R-MASS 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-mcmcplots 
Requires:         R-CRAN-rjags >= 3.4
Requires:         R-CRAN-R2jags >= 0.04.03
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggExtra 
Requires:         R-MASS 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-mcmcplots 

%description
Provides a new class of Bayesian meta-analysis models that we called "The
Hierarchical Meta-Regression" (HMR). The aim of HMR is to incorporate into
the meta-analysis, the data collection process, which results in a model
for the internal and external validity bias. In this way, it is possible
to combine studies of different types. For example, we can combine the
results of randomized control trials (RCTs) with the results of
observational studies (OS). The statistical methods and their applications
are described in Verde (2019) <doi:10.1002/bimj.201700266> and in Verde
(2017) <doi:10.5772/intechopen.70231>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
