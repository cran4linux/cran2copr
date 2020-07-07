%global packname  metaBMA
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          3%{?dist}
Summary:          Bayesian Model Averaging for Random and Fixed EffectsMeta-Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-logspline 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-bridgesampling 
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-logspline 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-bridgesampling 

%description
Computes the posterior model probabilities for standard meta-analysis
models (null model vs. alternative model assuming either fixed- or
random-effects, respectively). These posterior probabilities are used to
estimate the overall mean effect size as the weighted average of the mean
effect size estimates of the random- and fixed-effect model as proposed by
Gronau, Van Erp, Heck, Cesario, Jonas, & Wagenmakers (2017,
<doi:10.1080/23743603.2017.1326760>). The user can define a wide range of
non-informative or informative priors for the mean effect size and the
heterogeneity coefficient. Moreover, using pre-compiled Stan models,
meta-analysis with continuous and discrete moderators with
Jeffreys-Zellner-Siow (JZS) priors can be fitted and tested. This allows
to compute Bayes factors and perform Bayesian model averaging across
random- and fixed-effects meta-analysis with and without moderators. For a
primer on Bayesian model-averaged meta-analysis, see Gronau, Heck,
Berkhout, Haaf, & Wagenmakers (2020, <doi:10.31234/osf.io/97qup>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
