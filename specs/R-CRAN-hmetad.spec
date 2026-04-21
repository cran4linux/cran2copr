%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hmetad
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fit the Meta-D' Model of Confidence Ratings Using 'brms'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidybayes >= 3.0.7
BuildRequires:    R-CRAN-brms >= 2.23.0
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-posterior >= 1.6.1
BuildRequires:    R-CRAN-stringr >= 1.6.0
BuildRequires:    R-CRAN-abind >= 1.4.8
BuildRequires:    R-CRAN-tidyr >= 1.3.2
BuildRequires:    R-CRAN-dplyr >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.7
BuildRequires:    R-stats 
Requires:         R-CRAN-tidybayes >= 3.0.7
Requires:         R-CRAN-brms >= 2.23.0
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-posterior >= 1.6.1
Requires:         R-CRAN-stringr >= 1.6.0
Requires:         R-CRAN-abind >= 1.4.8
Requires:         R-CRAN-tidyr >= 1.3.2
Requires:         R-CRAN-dplyr >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.7
Requires:         R-stats 

%description
Implementation of Bayesian regressions over the meta-d' model of
psychological data from two alternative forced choice tasks with ordinal
confidence ratings. For more information, see Maniscalco & Lau (2012)
<doi:10.1016/j.concog.2011.09.021>. The package is a front-end to the
'brms' package, which facilitates a wide range of regression designs, as
well as tools for efficiently extracting posterior estimates, plotting,
and significance testing.

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
