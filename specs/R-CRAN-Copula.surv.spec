%global __brp_check_rpaths %{nil}
%global packname  Copula.surv
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Association Analysis of Bivariate Survival Data Based on Copulas

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Perform association analysis of bivariate survival data based on copula
models. Two different ways to estimate the association parameter in copula
models are implemented. A goodness-of-fit test for a given copula model is
implemented. See Emura, Lin and Wang (2010)
<doi:10.1016/j.csda.2010.03.013> for details. A more general reference for
the copula-based analysis of bivariate survival data is Emura, Matsui, and
Rondeau (2019) <doi:10.1007/978-981-13-3516-7>.

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
