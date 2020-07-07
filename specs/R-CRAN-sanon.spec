%global packname  sanon
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          3%{?dist}
Summary:          Stratified Analysis with Nonparametric Covariable Adjustment

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch

%description
There are several functions to implement the method for analysis in a
randomized clinical trial with strata with following key features. A
stratified Mann-Whitney estimator addresses the comparison between two
randomized groups for a strictly ordinal response variable. The
multivariate vector of such stratified Mann-Whitney estimators for
multivariate response variables can be considered for one or more response
variables such as in repeated measurements and these can have missing
completely at random (MCAR) data. Non-parametric covariance adjustment is
also considered with the minimal assumption of randomization. The p-value
for hypothesis test and confidence interval are provided.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
