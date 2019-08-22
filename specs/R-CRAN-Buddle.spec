%global packname  Buddle
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          A Deep Learning Package for Statistical Classification Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.17

%description
Statistical classification has been popular among various fields and
stayed in the limelight of scientists of those fields. Examples of the
fields include clinical trials where the statistical classification of
patients is indispensable to predict the clinical courses of diseases.
Considering the negative impact of diseases on performing daily tasks,
correctly classifying patients based on the clinical information is vital
in that we need to identify patients of the high-risk group to develop a
severe state and arrange medical treatment for them at an opportune
moment. Deep learning - a part of artificial intelligence - has gained
much attention, and research on it burgeons during past decades. It is a
veritable technique which was originally designed for the classification,
and hence, the EzDL package can provide sublime solutions to various
challenging classification problems encountered in the clinical trials.
The EzDL package is based on the back-propagation algorithm which performs
a multi-layer feed-forward neural network. This package contains two
functions: Buddle_Main() and Buddle_Predict(). Buddle_Main() builds a
feed-forward neural network model and trains the model. Buddle_Predict()
provokes the trained model which is the output of Buddle_Main(),
classifies given data, and make a final prediction for the data.

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
%{rlibdir}/%{packname}/libs
