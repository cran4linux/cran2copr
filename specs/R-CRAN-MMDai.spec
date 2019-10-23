%global packname  MMDai
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Multivariate Multinomial Distribution Approximation andImputation for Incomplete Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DirichletReg 
BuildRequires:    R-stats 
Requires:         R-CRAN-DirichletReg 
Requires:         R-stats 

%description
Missingness in categorical data is a common problem in various real
applications. Traditional approaches either utilize only the complete
observations or impute the missing data by some ad hoc methods rather than
the true conditional distribution of the missing data, thus losing or
distorting the rich information in the partial observations. This package
develops a Bayesian nonparametric approach, the Dirichlet Process Mixture
of Collapsed Product-Multinomials (DPMCPM, Wang et al. (2017)
<arXiv:1712.02214v1>), to model the full data jointly and compute the
model efficiently. By fitting an infinite mixture of product-multinomial
distributions, DPMCPM is applicable for any categorical data regardless of
the true distribution, which may contain complex association among
variables. Under the framework of latent class analysis, we show that
DPMCPM can model general missing mechanisms by creating an extra category
to denote missingness, which implicitly integrates out the missing part
with regard to their true conditional distribution.

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
