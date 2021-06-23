%global __brp_check_rpaths %{nil}
%global packname  BAS
%global packver   1.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Variable Selection and Model Averaging using BayesianAdaptive Sampling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Package for Bayesian Variable Selection and Model Averaging in linear
models and generalized linear models using stochastic or deterministic
sampling without replacement from posterior distributions.  Prior
distributions on coefficients are from Zellner's g-prior or mixtures of
g-priors corresponding to the Zellner-Siow Cauchy Priors or the mixture of
g-priors from Liang et al (2008) <DOI:10.1198/016214507000001337> for
linear models or mixtures of g-priors from Li and Clyde (2019)
<DOI:10.1080/01621459.2018.1469992> in generalized linear models. Other
model selection criteria include AIC, BIC and Empirical Bayes estimates of
g. Sampling probabilities may be updated based on the sampled models using
sampling w/out replacement or an efficient MCMC algorithm which samples
models using a tree structure of the model space as an efficient hash
table.  See Clyde, Ghosh and Littman (2010) <DOI:10.1198/jcgs.2010.09049>
for details on the sampling algorithms. Uniform priors over all models or
beta-binomial prior distributions on model size are allowed, and for large
p truncated priors on the model space may be used to enforce sampling
models that are full rank. The user may force variables to always be
included in addition to imposing constraints that higher order
interactions are included only if their parents are included in the model.
This material is based upon work supported by the National Science
Foundation under Division of Mathematical Sciences grant 1106891. Any
opinions, findings, and conclusions or recommendations expressed in this
material are those of the author(s) and do not necessarily reflect the
views of the National Science Foundation.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
