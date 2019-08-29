%global packname  bimixt
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Estimates Mixture Models for Case-Control Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-pROC 

%description
Estimates non-Gaussian mixture models of case-control data. The four types
of models supported are binormal, two component constrained, two component
unconstrained, and four component.  The most general model is the four
component model, under which both cases and controls are distributed
according to a mixture of two unimodal distributions.  In the four
component model, the two component distributions of the control mixture
may be distinct from the two components of the case mixture distribution.
In the two component unconstrained model, the components of the control
and case mixtures are the same; however the mixture probabilities may
differ for cases and controls.  In the two component constrained model,
all controls are distributed according to one of the two components while
cases follow a mixture distribution of the two components.  In the
binormal model, cases and controls are distributed according to distinct
unimodal distributions.  These models assume that Box-Cox transformed case
and control data with a common lambda parameter are distributed according
to Gaussian mixture distributions.  Model parameters are estimated using
the expectation-maximization (EM) algorithm.  Likelihood ratio test
comparison of nested models can be performed using the lr.test function.
AUC and PAUC values can be computed for the model-based and empirical ROC
curves using the auc and pauc functions, respectively. The model-based and
empirical ROC curves can be graphed using the roc.plot function. Finally,
the model-based density estimates can be visualized by plotting a model
object created with the bimixt.model function.

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
