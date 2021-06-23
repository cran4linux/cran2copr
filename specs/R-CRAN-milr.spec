%global __brp_check_rpaths %{nil}
%global packname  milr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple-Instance Logistic Regression with LASSO Penalty

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-pipeR >= 0.5
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-pipeR >= 0.5
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-utils 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-RcppParallel 

%description
The multiple instance data set consists of many independent subjects
(called bags) and each subject is composed of several components (called
instances). The outcomes of such data set are binary or categorical
responses, and, we can only observe the subject-level outcomes. For
example, in manufacturing processes, a subject is labeled as "defective"
if at least one of its own components is defective, and otherwise, is
labeled as "non-defective". The 'milr' package focuses on the predictive
model for the multiple instance data set with binary outcomes and performs
the maximum likelihood estimation with the Expectation-Maximization
algorithm under the framework of logistic regression. Moreover, the LASSO
penalty is attached to the likelihood function for simultaneous parameter
estimation and variable selection.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
