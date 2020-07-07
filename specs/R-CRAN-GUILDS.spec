%global packname  GUILDS
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}
Summary:          Implementation of Sampling Formulas for the Unified NeutralModel of Biodiversity and Biogeography, with or without GuildStructure

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-pracma 

%description
A collection of sampling formulas for the unified neutral model of
biogeography and biodiversity. Alongside the sampling formulas, it
includes methods to perform maximum likelihood optimization of the
sampling formulas, methods to generate data given the neutral model, and
methods to estimate the expected species abundance distribution. Sampling
formulas included in the GUILDS package are the Etienne Sampling Formula
(Etienne 2005), the guild sampling formula, where guilds are assumed to
differ in dispersal ability (Janzen et al. 2015), and the guilds sampling
formula conditioned on guild size (Janzen et al. 2015).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
