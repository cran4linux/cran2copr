%global packname  double.truncation
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Doubly-Truncated Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Likelihood-based inference methods with doubly-truncated data are
developed under various models. Nonparametric models are based on Efron
and Petrosian (1999) <doi:10.1080/01621459.1999.10474187> and Emura,
Konno, and Michimae (2015) <doi:10.1007/s10985-014-9297-5>. Parametric
models from the special exponential family (SEF) are based on Hu and Emura
(2015) <doi:10.1007/s00180-015-0564-z> and Emura, Hu and Konno (2017)
<doi:10.1007/s00362-015-0730-y>. The parametric location-scale models are
based on Dorre et al. (2020) <doi:10.1007/s00180-020-01027-6>.

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
