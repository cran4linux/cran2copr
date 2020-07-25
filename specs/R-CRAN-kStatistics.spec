%global packname  kStatistics
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Unbiased Estimators for Cumulant Products

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Tools for estimate (joint) cumulants and products of (joint) cumulants of
a given population distribution using (multivariate) k-statistics and
(multivariate) polykays, unbiased estimators with minimum variance. Tools
for generating univariate and multivariate Faa di Bruno's formula and
related polynomials, such as Bell polynomials, generalized complete Bell
polynomials, partition polynomials, generalized partition polynomials. For
more details see Di Nardo E., Guarino G., Senato D. (2009)
<arXiv:0807.5008>, <arXiv:1012.6008>.

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
