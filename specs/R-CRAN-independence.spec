%global packname  independence
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Rank-Based Independence Testing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-Rcpp >= 1.0.5

%description
Performs three ranking-based nonparametric tests for the independence of
two continuous variables: (1) the classical Hoeffding's D test; (2) a
refined variant of it, named R; (3) the Bergsma-Dassios T* sign
covariance. The first test is consistent assuming an absolutely continuous
bivariate distribution, i.e., the population coefficient D=0 iff the
variables are independent. The latter two are consistent under no
restriction on the distribution. All three statistics are computed in time
O(n log n) given n iid paired samples. The computation of R and T* uses a
new algorithm, following work of Even-Zohar and Leng (2019), see
<arXiv:1911.01414> and references therein.

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
