%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  copent
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Copula Entropy and Transfer Entropy

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-parallel 

%description
The nonparametric methods for estimating copula entropy, transfer entropy,
and the statistics for multivariate normality test and two-sample test are
implemented. The methods for estimating transfer entropy and the
statistics for multivariate normality test and two-sample test are based
on the method for estimating copula entropy. The method for change point
detection with copula entropy based two-sample test is also implemented.
Please refer to Ma and Sun (2011) <doi:10.1016/S1007-0214(11)70008-6>, Ma
(2019) <doi:10.48550/arXiv.1910.04375>, Ma (2022)
<doi:10.48550/arXiv.2206.05956>, Ma (2023)
<doi:10.48550/arXiv.2307.07247>, and Ma (2024)
<doi:10.48550/arXiv.2403.07892> for more information.

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
