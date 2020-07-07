%global packname  lrmest
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          2%{?dist}
Summary:          Different Types of Estimators to Deal with Multicollinearity

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-psych 
Requires:         R-MASS 
Requires:         R-CRAN-psych 

%description
When multicollinearity exists among predictor variables of the linear
model, least square estimators does not provide a better solution for
estimating parameters. To deal with multicollinearity several estimators
are proposed in the literature. Some of these estimators are Ordinary
Least Square Estimator (OLSE), Ordinary Generalized Ordinary Least Square
Estimator (OGOLSE), Ordinary Ridge Regression Estimator (ORRE), Ordinary
Generalized Ridge Regression Estimator (OGRRE), Restricted Least Square
Estimator (RLSE), Ordinary Generalized Restricted Least Square Estimator
(OGRLSE), Ordinary Mixed Regression Estimator (OMRE), Ordinary Generalized
Mixed Regression Estimator (OGMRE), Liu Estimator (LE), Ordinary
Generalized Liu Estimator (OGLE), Restricted Liu Estimator (RLE), Ordinary
Generalized Restricted Liu Estimator (OGRLE), Stochastic Restricted Liu
Estimator (SRLE), Ordinary Generalized Stochastic Restricted Liu Estimator
(OGSRLE), Type (1),(2),(3) Liu Estimator (Type-1,2,3 LTE), Ordinary
Generalized Type (1),(2),(3) Liu Estimator (Type-1,2,3 OGLTE), Type
(1),(2),(3) Adjusted Liu Estimator (Type-1,2,3 ALTE), Ordinary Generalized
Type (1),(2),(3) Adjusted Liu Estimator (Type-1,2,3 OGALTE), Almost
Unbiased Ridge Estimator (AURE), Ordinary Generalized Almost Unbiased
Ridge Estimator (OGAURE), Almost Unbiased Liu Estimator (AULE), Ordinary
Generalized Almost Unbiased Liu Estimator (OGAULE), Stochastic Restricted
Ridge Estimator (SRRE), Ordinary Generalized Stochastic Restricted Ridge
Estimator (OGSRRE), Restricted Ridge Regression Estimator (RRRE) and
Ordinary Generalized Restricted Ridge Regression Estimator (OGRRRE). To
select the best estimator in a practical situation the Mean Square Error
(MSE) is used. Using this package scalar MSE value of all the above
estimators and Prediction Sum of Square (PRESS) values of some of the
estimators can be obtained, and the variation of the MSE and PRESS values
for the relevant estimators can be shown graphically.

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

%files
%{rlibdir}/%{packname}
