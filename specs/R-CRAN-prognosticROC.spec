%global packname  prognosticROC
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}
Summary:          Prognostic ROC curves for evaluating the predictive capacity ofa binary test

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-survival 
Requires:         R-splines 
Requires:         R-survival 

%description
Prognostic ROC curve is an alternative graphical approach to represent the
discriminative capacity of the marker: a receiver operating characteristic
(ROC) curve by plotting 1 minus the survival in the high-risk group
against 1 minus the survival in the low-risk group. This package contains
functions to assess prognostic ROC curve. The user can enter the survival
according to a model previously estimated or the user can also enter
individual survival data for estimating the prognostic ROC curve by using
Kaplan-Meier estimator. The area under the curve (AUC) corresponds to the
probability that a patient in the low-risk group has a longer lifetime
than a patient in the high-risk group. The prognostic ROC curve provides
complementary information compared to survival curves. The AUC is assessed
by using the trapezoidal rules. When survival curves do not reach 0, the
prognostic ROC curve is incomplete and the extrapolations of the AUC are
performed by assuming pessimist, optimist and non-informative situations.

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
%{rlibdir}/%{packname}/INDEX
