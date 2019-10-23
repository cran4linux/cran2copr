%global packname  ROC632
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          Construction of diagnostic or prognostic scoring system andinternal validation of its discriminative capacities based onROC curve and 0.633+ boostrap resampling.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-penalized 
BuildRequires:    R-CRAN-survivalROC 
Requires:         R-splines 
Requires:         R-survival 
Requires:         R-CRAN-penalized 
Requires:         R-CRAN-survivalROC 

%description
This package computes traditional ROC curves and time-dependent ROC curves
using the cross-validation, the 0.632 and the 0.632+ estimators. The
0.632+ estimator of time-dependent ROC curve is useful to estimate the
predictive accuracy of prognostic signature based on high-dimensional
data. For instance, it outperforms the other approaches, especially the
cross-validation solution which is often used. The 0.632+ estimators
correct the area under the curve in order to adequately estimate the
prognostic capacities regardless of the overfitting level. This package
also allows for the construction of diagnostic or prognostic scoring
systems (penalized regressions). The methodology is adapted to complete
data (penalized logistic regression associated with ROC curve) or
incomplete time-to-event data (penalized Cox model associated with
time-dependent ROC curve).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
