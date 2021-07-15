%global __brp_check_rpaths %{nil}
%global packname  robustMVMR
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Perform the Robust Multivariable Mendelian Randomization Analysis

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.6.2
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-robustbase >= 0.93.5
BuildRequires:    R-CRAN-lmtest >= 0.9.37
Requires:         R-stats >= 3.6.2
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-robustbase >= 0.93.5
Requires:         R-CRAN-lmtest >= 0.9.37

%description
Perform the robust multivariable Mendelian randomization 'robustMVMR'
analysis in the two-sample Mendelian randomization setting. An example
paper using the 'robustMVMR' package can be found in Yang et al. (2021)
<doi:10.1080/15412555.2021.1955848>. In details, the 'robustMVMR' package
produces both the robust estimators and the robust standard errors via the
MM-estimates, which has been demonstrated to protect against
heteroskedasticity, autocorrelation, and the presence of outliers in Yohai
(1987) <doi:10.1214/aos/1176350366> and Croux (2003)
<https://EconPapers.repec.org/RePEc:ete:ceswps:ces0316>.

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
