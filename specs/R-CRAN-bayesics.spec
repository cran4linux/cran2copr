%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesics
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analyses for One- and Two-Sample Inference and Regression Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-BMS 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-DFBA 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-BMS 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-DFBA 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-survival 

%description
Perform fundamental analyses using Bayesian parametric and non-parametric
inference (regression, anova, 1 and 2 sample inference, non-parametric
tests, etc.).  (Practically) no Markov chain Monte Carlo (MCMC) is used;
all exact finite sample inference is completed via closed form solutions
or else through posterior sampling automated to ensure precision in
interval estimate bounds. Diagnostic plots for model assessment, and key
inferential quantities (point and interval estimates, probability of
direction, region of practical equivalence, and Bayes factors) and model
visualizations are provided. Bayes factors are computed either by the
Savage Dickey ratio given in Dickey (1971) <doi:10.1214/aoms/1177693507>
or by Chib's method as given in xxx. Interpretations are from Kass and
Raftery (1995) <doi:10.1080/01621459.1995.10476572>.  ROPE bounds are
based on discussions in Kruschke (2018) <doi:10.1177/2515245918771304>.
Methods for determining the number of posterior samples required are
described in Doss et al. (2014) <doi:10.1214/14-EJS957>. Bayesian model
averaging is done in part by Feldkircher and Zeugner (2015)
<doi:10.18637/jss.v068.i04>. Methods for contingency table analysis is
described in Gunel et al. (1974) <doi:10.1093/biomet/61.3.545>.
Variational Bayes (VB) methods are described in Salimans and Knowles
(2013) <doi:10.1214/13-BA858>. Mediation analysis uses the framework
described in Imai et al. (2010) <doi:10.1037/a0020761>. The
loss-likelihood bootstrap used in the non-parametric regression modeling
is described in Lyddon et al. (2019) <doi:10.1093/biomet/asz006>.
Non-parametric survival methods are described in Qing et al. (2023)
<doi:10.1002/pst.2256>. Methods used for the Bayesian Wilcoxon signed-rank
analysis is given in Chechile (2018) <doi:10.1080/03610926.2017.1388402>
and for the Bayesian Wilcoxon rank sum analysis in Chechile (2020)
<doi:10.1080/03610926.2018.1549247>.  Correlation analysis methods are
carried out by Barch and Chechile (2023) <doi:10.32614/CRAN.package.DFBA>,
and described in Lindley and Phillips (1976)
<doi:10.1080/00031305.1976.10479154> and Chechile and Barch (2021)
<doi:10.1016/j.jmp.2021.102638>.  See also Chechile (2020, ISBN:
9780262044585).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
