%global packname  GHS
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          Graphical Horseshoe MCMC Sampler Using Data Augmented BlockGibbs Sampler

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-MASS 

%description
Draw posterior samples to estimate the precision matrix for multivariate
Gaussian data. Posterior means of the samples is the graphical horseshoe
estimate by Li, Bhadra and Craig(2017) <arXiv:1707.06661>. The function
uses matrix decomposition and variable change from the Bayesian graphical
lasso by Wang(2012) <doi:10.1214/12-BA729>, and the variable augmentation
for sampling under the horseshoe prior by Makalic and Schmidt(2016)
<arXiv:1508.03884>. Structure of the graphical horseshoe function was
inspired by the Bayesian graphical lasso function using blocked sampling,
authored by Wang(2012) <doi:10.1214/12-BA729>.

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
