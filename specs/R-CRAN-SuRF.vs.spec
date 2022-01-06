%global __brp_check_rpaths %{nil}
%global packname  SuRF.vs
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Subsampling Ranking Forward Selection (SuRF)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 

%description
Performs variable selection based on subsampling, ranking forward
selection. Xo is the matrix of predictor variables. y is the response
variable. Currently only binary responses using logistic regression are
supported. X is a matrix of additional predictors which should be scaled
to have sum 1 prior to analysis. fold is the number of folds for
cross-validation. Alpha is the parameter for the elastic net method used
in the subsampling procedure: the default value of 1 corresponds to LASSO.
prop is the proportion of variables to remove in the each subsample.
weights indicates whether observations should be weighted by class size.
When the class sizes are unbalanced, weighting observations can improve
results. B is the number of subsamples to use for ranking the variables. C
is the number of permutations to use for estimating the critical value of
the null distribution. If the 'doParallel' package is installed, the
function can be run in parallel by setting ncores to the number of threads
to use. If the default value of 1 is used, or if the 'doParallel' package
is not installed, the function does not run in parallel. display.progress
indicates whether the function should display messages indicating its
progress. family is a family variable for the glm() fitting. Note that the
'glmnet' package does not permit the use of nonstandard link functions, so
will always use the default link function. However, the glm() fitting will
use the specified link. The default is binomial with logistic regression,
because this is a common use case. pval is the p-value for inclusion of a
variable in the model. Under the null case, the number of false positives
will be geometrically distributed with this as probability of success, so
if this parameter is set to p, the expected number of false positives
should be p/(1-p).

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
