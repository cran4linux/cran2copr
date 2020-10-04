%global packname  adaptMCMC
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Implementation of a Generic Adaptive Monte Carlo Markov ChainSampler

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-coda 
Requires:         R-Matrix 

%description
Enables sampling from arbitrary distributions if the log density is known
up to a constant; a common situation in the context of Bayesian inference.
The implemented sampling algorithm was proposed by Vihola (2012)
<DOI:10.1007/s11222-011-9269-5> and achieves often a high efficiency by
tuning the proposal distributions to a user defined acceptance rate.

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
%{rlibdir}/%{packname}/INDEX
