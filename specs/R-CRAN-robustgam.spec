%global packname  robustgam
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Estimation for Generalized Additive Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-mgcv >= 1.7.20
BuildRequires:    R-CRAN-robustbase >= 0.9.3
BuildRequires:    R-CRAN-Rcpp >= 0.9.13
BuildRequires:    R-CRAN-RcppArmadillo >= 0.3.4.4
Requires:         R-mgcv >= 1.7.20
Requires:         R-CRAN-robustbase >= 0.9.3
Requires:         R-CRAN-Rcpp >= 0.9.13
Requires:         R-CRAN-RcppArmadillo >= 0.3.4.4

%description
This package provides robust estimation for generalized additive models.
It implements a fast and stable algorithm in Wong, Yao and Lee (2013). The
implementation also contains three automatic selection methods for
smoothing parameter. They are designed to be robust to outliers. For more
details, see Wong, Yao and Lee (2013).

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
