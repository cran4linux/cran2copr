%global __brp_check_rpaths %{nil}
%global packname  RGeode
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geometric Density Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-MASS >= 7.3.47
BuildRequires:    R-stats >= 3.4.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
Requires:         R-MASS >= 7.3.47
Requires:         R-stats >= 3.4.1
Requires:         R-CRAN-Rcpp >= 0.12.11

%description
Provides the hybrid Bayesian method Geometric Density Estimation. On the
one hand, it scales the dimension of our data, on the other it performs
inference. The method is fully described in the paper "Scalable Geometric
Density Estimation" by Y. Wang, A. Canale, D. Dunson (2016)
<http://proceedings.mlr.press/v51/wang16e.pdf>.

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
