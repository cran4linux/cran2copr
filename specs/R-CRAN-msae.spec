%global packname  msae
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Multivariate Fay Herriot Models for Small Area Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-magic 
Requires:         R-CRAN-magic 

%description
Implements multivariate Fay-Herriot models for small area estimation. It
uses empirical best linear unbiased prediction (EBLUP) estimator.
Multivariate models consider the correlation of several target variables
and borrow strength from auxiliary variables to improve the effectiveness
of a domain sample size. Models which accommodated by this package are
univariate model with several target variables (model 0), multivariate
model (model 1), autoregressive multivariate model (model 2), and
heteroscedastic autoregressive multivariate model (model 3). Functions
provide EBLUP estimators and mean squared error (MSE) estimator for each
model. These models were developed by Roberto Benavent and Domingo Morales
(2015) <doi:10.1016/j.csda.2015.07.013>.

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
%{rlibdir}/%{packname}/INDEX
