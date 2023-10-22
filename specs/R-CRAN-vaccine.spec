%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vaccine
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for Immune Correlates Analysis of Vaccine Clinical Trial Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-earth >= 5.3.1
BuildRequires:    R-methods >= 4.2.2
BuildRequires:    R-splines >= 4.2.2
BuildRequires:    R-stats >= 4.2.2
BuildRequires:    R-CRAN-glmnet >= 4.1.6
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-survival >= 3.4.0
BuildRequires:    R-CRAN-SuperLearner >= 2.0.28
BuildRequires:    R-CRAN-e1071 >= 1.7.12
BuildRequires:    R-CRAN-fdrtool >= 1.2.17
BuildRequires:    R-CRAN-Rsolnp >= 1.16
BuildRequires:    R-CRAN-truncnorm >= 1.0.8
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-ggpubr >= 0.5.0
BuildRequires:    R-CRAN-simest >= 0.4
BuildRequires:    R-CRAN-survML >= 0.0.0.9000
Requires:         R-CRAN-earth >= 5.3.1
Requires:         R-methods >= 4.2.2
Requires:         R-splines >= 4.2.2
Requires:         R-stats >= 4.2.2
Requires:         R-CRAN-glmnet >= 4.1.6
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-survival >= 3.4.0
Requires:         R-CRAN-SuperLearner >= 2.0.28
Requires:         R-CRAN-e1071 >= 1.7.12
Requires:         R-CRAN-fdrtool >= 1.2.17
Requires:         R-CRAN-Rsolnp >= 1.16
Requires:         R-CRAN-truncnorm >= 1.0.8
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-ggpubr >= 0.5.0
Requires:         R-CRAN-simest >= 0.4
Requires:         R-CRAN-survML >= 0.0.0.9000

%description
Various semiparametric and nonparametric statistical tools for immune
correlates analysis of vaccine clinical trial data. This includes
calculation of summary statistics and estimation of risk, vaccine
efficacy, controlled risk, and controlled vaccine efficacy. See Gilbert P,
Fong Y, Kenny A, and Carone, M (2022) <doi:10.1093/biostatistics/kxac24>.

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
