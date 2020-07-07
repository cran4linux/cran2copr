%global packname  CoinMinD
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Simultaneous Confidence Interval for Multinomial Proportion

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-CRAN-MCMCpack 

%description
Methods for obtaining simultaneous confidence interval for multinomial
proportion have been proposed by many authors and the present study
include a variety of widely applicable procedures. Seven classical methods
(Wilson, Quesenberry and Hurst, Goodman, Wald with and without continuity
correction, Fitzpatrick and Scott, Sison and Glaz) and Bayesian Dirichlet
models are included in the package. The advantage of MCMC pack has been
exploited to derive the Dirichlet posterior directly and this also helps
in handling the Dirichlet prior parameters. This package is prepared to
have equal and unequal values for the Dirichlet prior distribution that
will provide better scope for data analysis and associated sensitivity
analysis.

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
