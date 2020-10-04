%global packname  mhazard
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Survival Function Estimation and Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-boot 
Requires:         R-CRAN-plot3D 
Requires:         R-survival 
Requires:         R-CRAN-rootSolve 

%description
Estimates the survival function and Cox regression parameters for the
multivariate survival setting where there are multiple (right-censored)
outcome variables. The Volterra, Dabrowska, and Prentice-Cai estimates of
the bivariate survival function may be computed as well as the Dabrowska
estimate of the trivariate survival function. Bivariate Cox regression
estimates can also be computed. Functions are also provided to compute
(bootstrap) confidence intervals and plot the estimates of the bivariate
survival function. For details, see "The Statistical Analysis of
Multivariate Failure Time Data: A Marginal Modeling Approach", Prentice,
R., Zhao, S. (2019, ISBN: 978-1-4822-5657-4), CRC Press.

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
