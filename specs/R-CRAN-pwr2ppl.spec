%global __brp_check_rpaths %{nil}
%global packname  pwr2ppl
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analyses for Common Designs (Power to the People)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51
BuildRequires:    R-CRAN-quantreg >= 5.50
BuildRequires:    R-CRAN-MBESS >= 4.5.0
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-nlme >= 3.1.139
BuildRequires:    R-CRAN-car >= 3.0.0
BuildRequires:    R-CRAN-lmtest >= 0.9.30
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-tidyr >= 0.8.0
BuildRequires:    R-CRAN-broom >= 0.7.00
BuildRequires:    R-CRAN-lavaan >= 0.6.2
BuildRequires:    R-CRAN-semTools >= 0.5
BuildRequires:    R-CRAN-ez >= 0.4.3
BuildRequires:    R-CRAN-afex >= 0.22.1
BuildRequires:    R-CRAN-phia >= 0.2.0
Requires:         R-CRAN-MASS >= 7.3.51
Requires:         R-CRAN-quantreg >= 5.50
Requires:         R-CRAN-MBESS >= 4.5.0
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-nlme >= 3.1.139
Requires:         R-CRAN-car >= 3.0.0
Requires:         R-CRAN-lmtest >= 0.9.30
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-tidyr >= 0.8.0
Requires:         R-CRAN-broom >= 0.7.00
Requires:         R-CRAN-lavaan >= 0.6.2
Requires:         R-CRAN-semTools >= 0.5
Requires:         R-CRAN-ez >= 0.4.3
Requires:         R-CRAN-afex >= 0.22.1
Requires:         R-CRAN-phia >= 0.2.0

%description
Statistical power analysis for designs including t-tests, correlations,
multiple regression, ANOVA, mediation, and logistic regression. Functions
accompany Aberson (2019) <doi:10.4324/9781315171500>.

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
