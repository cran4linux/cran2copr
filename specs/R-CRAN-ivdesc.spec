%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ivdesc
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Profiling Compliers and Non-Compliers for Instrumental Variable Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-rsample >= 0.0.3
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-rsample >= 0.0.3

%description
Estimating the mean and variance of a covariate for the complier,
never-taker and always-taker subpopulation in the context of instrumental
variable estimation. This package implements the method described in
Marbach and Hangartner (2020) <doi:10.1017/pan.2019.48> and Hangartner,
Marbach, Henckel, Maathuis, Kelz and Keele (2021)
<doi:10.48550/arXiv.2103.06328>.

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
