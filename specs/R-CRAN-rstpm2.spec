%global packname  rstpm2
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          3%{?dist}
Summary:          Smooth Survival Models, Including Generalized Survival Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-bbmle >= 1.0.20
BuildRequires:    R-CRAN-Rcpp >= 0.10.2
BuildRequires:    R-methods 
BuildRequires:    R-survival 
BuildRequires:    R-splines 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-bbmle >= 1.0.20
Requires:         R-CRAN-Rcpp >= 0.10.2
Requires:         R-methods 
Requires:         R-survival 
Requires:         R-splines 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-mgcv 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-deSolve 
Requires:         R-utils 
Requires:         R-parallel 

%description
R implementation of generalized survival models (GSMs), smooth accelerated
failure time (AFT) models and Markov multi-state models. For the GSMs,
g(S(t|x))=eta(t,x) for a link function g, survival S at time t with
covariates x and a linear predictor eta(t,x). The main assumption is that
the time effect(s) are smooth <doi:10.1177/0962280216664760>. For fully
parametric models with natural splines, this re-implements Stata's 'stpm2'
function, which are flexible parametric survival models developed by
Royston and colleagues. We have extended the parametric models to include
any smooth parametric smoothers for time. We have also extended the model
to include any smooth penalized smoothers from the 'mgcv' package, using
penalized likelihood. These models include left truncation, right
censoring, interval censoring, gamma frailties and normal random effects
<doi:10.1002/sim.7451>. For the smooth AFTs, S(t|x) = S_0(t*eta(t,x)),
where the baseline survival function S_0(t)=exp(-exp(eta_0(t))) is
modelled for natural splines for eta_0, and the time-dependent cumulative
acceleration factor eta(t,x)=int_0^t exp(eta_1(u,x)) du for log
acceleration factor eta_1(u,x). The Markov multi-state models allow for a
range of models with smooth transitions to predict transition
probabilities, length of stay, utilities and costs, with differences,
ratios and standardisation.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/aft.aux
%doc %{rlibdir}/%{packname}/aft.pdf
%doc %{rlibdir}/%{packname}/auto
%doc %{rlibdir}/%{packname}/competing_risks.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/fig1-README.md.jpg
%doc %{rlibdir}/%{packname}/fig2-README.md.jpg
%doc %{rlibdir}/%{packname}/math.aux
%doc %{rlibdir}/%{packname}/math.fdb_latexmk
%doc %{rlibdir}/%{packname}/math.fls
%doc %{rlibdir}/%{packname}/math.html
%doc %{rlibdir}/%{packname}/math.input
%doc %{rlibdir}/%{packname}/math.org
%doc %{rlibdir}/%{packname}/math.out
%doc %{rlibdir}/%{packname}/math.toc
%doc %{rlibdir}/%{packname}/model.bug
%doc %{rlibdir}/%{packname}/pstpm2.out
%doc %{rlibdir}/%{packname}/Rcpp-tests.R
%doc %{rlibdir}/%{packname}/test.do
%doc %{rlibdir}/%{packname}/Thumbs.db
%doc %{rlibdir}/%{packname}/tutorial
%doc %{rlibdir}/%{packname}/tvc-cox.R
%doc %{rlibdir}/%{packname}/unitTests
%doc %{rlibdir}/%{packname}/working_code.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
