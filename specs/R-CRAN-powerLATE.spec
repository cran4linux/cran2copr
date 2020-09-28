%global packname  powerLATE
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Power Analysis for LATE

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
An implementation of the generalized power analysis for the local average
treatment effect (LATE), proposed by Bansak (2020)
<doi:10.1214/19-STS732>. Power analysis is in the context of estimating
the LATE (also known as the complier average causal effect, or CACE), with
calculations based on a test of the null hypothesis that the LATE equals 0
with a two-sided alternative. The method uses standardized effect sizes to
place a conservative bound on the power under minimal assumptions. Package
allows users to recover power, sample size requirements, or minimum
detectable effect sizes. Package also allows users to work with absolute
effects rather than effect sizes, to specify an additional assumption to
narrow the bounds, and to incorporate covariate adjustment.

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
