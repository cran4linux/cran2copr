%global packname  MCMC.qpcr
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          2%{?dist}
Summary:          Bayesian Analysis of qRT-PCR Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCglmm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-MCMCglmm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-coda 

%description
Quantitative RT-PCR data are analyzed using generalized linear mixed
models based on lognormal-Poisson error distribution, fitted using MCMC.
Control genes are not required but can be incorporated as Bayesian priors
or, when template abundances correlate with conditions, as trackers of
global effects (common to all genes). The package also implements a
lognormal model for higher-abundance data and a "classic" model involving
multi-gene normalization on a by-sample basis. Several plotting functions
are included to extract and visualize results. The detailed tutorial is
available here:
<https://matzlab.weebly.com/uploads/7/6/2/2/76229469/mcmc.qpcr.tutorial.v1.2.4.pdf>.

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
%{rlibdir}/%{packname}/INDEX
