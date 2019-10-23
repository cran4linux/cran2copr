%global packname  Wrapped
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Computes Pdf, Cdf, Quantile, Random Numbers and ProvidesEstimation for any Univariate Wrapped Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-metRology 
BuildRequires:    R-CRAN-AdequacyModel 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-ald 
BuildRequires:    R-CRAN-NormalLaplace 
BuildRequires:    R-CRAN-GeneralizedHyperbolic 
BuildRequires:    R-CRAN-glogis 
BuildRequires:    R-CRAN-irtProb 
BuildRequires:    R-CRAN-sld 
BuildRequires:    R-CRAN-normalp 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-sgt 
BuildRequires:    R-CRAN-SkewHyperbolic 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-cubfits 
BuildRequires:    R-CRAN-lqmm 
BuildRequires:    R-CRAN-LCA 
BuildRequires:    R-CRAN-GEVStableGarch 
BuildRequires:    R-CRAN-VarianceGamma 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-ordinal 
Requires:         R-CRAN-metRology 
Requires:         R-CRAN-AdequacyModel 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-ald 
Requires:         R-CRAN-NormalLaplace 
Requires:         R-CRAN-GeneralizedHyperbolic 
Requires:         R-CRAN-glogis 
Requires:         R-CRAN-irtProb 
Requires:         R-CRAN-sld 
Requires:         R-CRAN-normalp 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-sgt 
Requires:         R-CRAN-SkewHyperbolic 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-cubfits 
Requires:         R-CRAN-lqmm 
Requires:         R-CRAN-LCA 
Requires:         R-CRAN-GEVStableGarch 
Requires:         R-CRAN-VarianceGamma 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-ordinal 

%description
Computes the pdf, cdf, quantile, random numbers for any wrapped G
distributions.  Computes maximum likelihood estimates of the parameters,
standard errors, 95 percent confidence intervals, value of Cramer-von
Misses statistic, value of Anderson Darling statistic, value of Kolmogorov
Smirnov test statistic and its $p$-value, value of Akaike Information
Criterion, value of Consistent Akaike Information Criterion, value of
Bayesian Information Criterion, value of Hannan-Quinn information
criterion, minimum value of the negative log-likelihood function and
convergence status when the wrapped distribution is fitted to some data.

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
