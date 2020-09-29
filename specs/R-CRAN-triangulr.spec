%global packname  triangulr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          High-Performance Triangular Distribution Functions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-vctrs >= 0.3.4
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-vctrs >= 0.3.4

%description
A collection of high-performance functions for the triangular distribution
that consists of the probability density function, cumulative distribution
function, quantile function, random variate generator, moment generating
function, characteristic function, and expected shortfall function.
References: Samuel Kotz, Johan Ren Van Dorp (2004) <doi:10.1142/5720> and
Acerbi, Carlo & Tasche, Dirk. (2002) <doi:10.1111/1468-0300.00091>.

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
