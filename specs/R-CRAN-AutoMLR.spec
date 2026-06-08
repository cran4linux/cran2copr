%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AutoMLR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Multi-Outcome Machine Learning Combination Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-survival 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides automated machine learning workflows for survival analysis,
binary classification, continuous outcomes, and ordinal outcomes. The
package trains and combines model variants across user-supplied
multi-cohort data, evaluates survival models by leave-one-out
cross-validation using Harrell's concordance index, binary models by
leave-one-out cross-validation using receiver operating characteristic
area under the curve, continuous models by out-of-fold root mean squared
error and R-squared, and ordinal models by out-of-fold quadratic weighted
kappa. It renders reproducible reports in Hypertext Markup Language (HTML)
with figures and diagnostics. The survival workflow supports penalized and
tree-based Cox proportional hazards models, stepwise Cox models, partial
least squares regression for Cox models, supervised principal components,
gradient boosting machine Cox models, survival support vector machines
(survival-SVM), random survival forests, and optional 'CoxBoost'. The
binary workflow supports penalized logistic regression, logistic
baselines, gradient boosting machines, random forests, principal component
analysis (PCA) logistic regression, and Gaussian naive Bayes variants.
Continuous and ordinal workflows reuse an 18-variant regression registry
with penalized, linear, boosted, forest, PCA, and baseline families. The
optional 'CoxBoost' model is enabled when the suggested 'CoxBoost' package
is installed; it is used conditionally and is not a strong dependency.
Optional model backends are checked at run time so missing backend
packages skip only the affected model variants rather than blocking
installation of the whole package. Methods build on Friedman et al. (2010)
<doi:10.18637/jss.v033.i01>, Bair and Tibshirani (2004)
<doi:10.1371/journal.pbio.0020108>, Ishwaran et al. (2008)
<doi:10.1214/08-AOAS169>, Blanche et al. (2013) <doi:10.1002/sim.5958>,
and Binder and Schumacher (2008) <doi:10.1186/1471-2105-9-14>.

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
