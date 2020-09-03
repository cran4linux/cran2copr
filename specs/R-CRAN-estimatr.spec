%global packname  estimatr
%global packver   0.24.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.24.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Estimators for Design-Based Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-generics 
Requires:         R-methods 

%description
Fast procedures for small set of commonly-used, design-appropriate
estimators with robust standard errors and confidence intervals. Includes
estimators for linear regression, instrumental variables regression,
difference-in-means, Horvitz-Thompson estimation, and regression improving
precision of experimental estimates by interacting treatment with centered
pre-treatment covariates introduced by Lin (2013)
<doi:10.1214/12-AOAS583>.

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
