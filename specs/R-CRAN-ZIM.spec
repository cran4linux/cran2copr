%global packname  ZIM
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Zero-Inflated Models (ZIM) for Count Time Series with ExcessZeros

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
Analyze count time series with excess zeros. Two types of statistical
models are supported: Markov regression by Yang et al. (2013)
<doi:10.1016/j.stamet.2013.02.001> and state-space models by Yang et al.
(2015) <doi:10.1177/1471082X14535530>. They are also known as
observation-driven and parameter-driven models respectively in the time
series literature. The functions used for Markov regression or
observation-driven models can also be used to fit ordinary regression
models with independent data under the zero-inflated Poisson (ZIP) or
zero-inflated negative binomial (ZINB) assumption. Besides, the package
contains some miscellaneous functions to compute density, distribution,
quantile, and generate random numbers from ZIP and ZINB distributions.

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
