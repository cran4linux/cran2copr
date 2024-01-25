%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gldrm
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Linear Density Ratio Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-stats >= 3.2.2
BuildRequires:    R-graphics >= 3.2.2
Requires:         R-stats >= 3.2.2
Requires:         R-graphics >= 3.2.2

%description
Fits a generalized linear density ratio model (GLDRM). A GLDRM is a
semiparametric generalized linear model. In contrast to a GLM, which
assumes a particular exponential family distribution, the GLDRM uses a
semiparametric likelihood to estimate the reference distribution. The
reference distribution may be any discrete, continuous, or mixed
exponential family distribution. The model parameters, which include both
the regression coefficients and the cdf of the unspecified reference
distribution, are estimated by maximizing a semiparametric likelihood.
Regression coefficients are estimated with no loss of efficiency, i.e. the
asymptotic variance is the same as if the true exponential family
distribution were known. Huang (2014) <doi:10.1080/01621459.2013.824892>.
Huang and Rathouz (2012) <doi:10.1093/biomet/asr075>. Rathouz and Gao
(2008) <doi:10.1093/biostatistics/kxn030>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
