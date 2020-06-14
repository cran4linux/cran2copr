%global packname  MfUSampler
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          2%{?dist}
Summary:          Multivariate-from-Univariate (MfU) MCMC Sampler

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ars 
BuildRequires:    R-CRAN-HI 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-ars 
Requires:         R-CRAN-HI 
Requires:         R-CRAN-coda 

%description
Convenience functions for multivariate MCMC using univariate samplers
including: slice sampler with stepout and shrinkage (Neal (2003)
<DOI:10.1214/aos/1056562461>), adaptive rejection sampler (Gilks and Wild
(1992) <DOI:10.2307/2347565>), adaptive rejection Metropolis (Gilks et al
(1995) <DOI:10.2307/2986138>), and univariate Metropolis with Gaussian
proposal.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
