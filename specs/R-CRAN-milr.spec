%global packname  milr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Multiple-Instance Logistic Regression with LASSO Penalty

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
