%global packname  logistf
%global packver   1.23.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.23.1
Release:          1%{?dist}%{?buildtag}
Summary:          Firth's Bias-Reduced Logistic Regression

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-mgcv 
Requires:         R-CRAN-mice 
Requires:         R-mgcv 

%description
Fit a logistic regression model using Firth's bias reduction method,
equivalent to penalization of the log-likelihood by the Jeffreys prior.
Confidence intervals for regression coefficients can be computed by
penalized profile likelihood. Firth's method was proposed as ideal
solution to the problem of separation in logistic regression. If needed,
the bias reduction can be turned off such that ordinary maximum likelihood
logistic regression is obtained.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
