%global packname  lchemix
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Bayesian Multi-Dimensional Couple-Based Latent Risk Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mvtnorm 

%description
A joint latent class model where a hierarchical structure exists, with an
interaction between female and male partners of a couple. A Bayesian
perspective to inference and Markov chain Monte Carlo algorithms to obtain
posterior estimates of model parameters. The reference paper is: Beom Seuk
Hwang, Zhen Chen, Germaine M.Buck Louis, Paul S. Albert, (2018) "A
Bayesian multi-dimensional couple-based latent risk model with an
application to infertility". Biometrics, 75, 315-325.
<doi:10.1111/biom.12972>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
