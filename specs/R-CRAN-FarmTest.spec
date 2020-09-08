%global packname  FarmTest
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Factor-Adjusted Robust Multiple Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-graphics 

%description
Performs robust multiple testing for means in the presence of known and
unknown latent factors presented in Fan et al.(2019) "FarmTest:
Factor-Adjusted Robust Multiple Testing With Approximate False Discovery
Control" <doi:10.1080/01621459.2018.1527700>. Implements a series of
adaptive Huber methods combined with fast data-drive tuning schemes
proposed in Ke et al.(2019) "User-Friendly Covariance Estimation for
Heavy-Tailed Distributions" <doi:10.1214/19-STS711> to estimate model
parameters and construct test statistics that are robust against
heavy-tailed and/or asymmetric error distributions. Extensions to
two-sample simultaneous mean comparison problems are also included. As
by-products, this package contains functions that compute adaptive Huber
mean, covariance and regression estimators that are of independent
interest.

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
