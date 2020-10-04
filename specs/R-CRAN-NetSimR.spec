%global packname  NetSimR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Actuarial Functions for Non-Life Insurance Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Assists actuaries and other insurance modellers in pricing, reserving and
capital modelling for non-life insurance and reinsurance modelling.
Provides functions that help model excess levels, capping and pure
Incurred but not reported claims (pure IBNR). Includes capped mean,
exposure curves and increased limit factor curves (ILFs) for LogNormal,
Gamma, Pareto, Sliced LogNormal-Pareto and Sliced Gamma-Pareto
distributions. Includes mean, probability density function (pdf),
cumulative probability function (cdf) and inverse cumulative probability
function for Sliced LogNormal-Pareto and Sliced Gamma-Pareto
distributions. Includes calculating pure IBNR exposure with LogNormal and
Gamma distribution for reporting delay.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
