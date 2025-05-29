%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MVN
%global packver   6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Normality Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-plotly 
Requires:         R-methods 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-plotly 

%description
A suite of multivariate normality tests (Mardia, Henze–Zirkler, Royston,
Doornik–Hansen, Energy), univariate diagnostics, robust outlier detection,
bivariate density plots, and Box–Cox transformations (Korkmaz et al,
(2014),
<https://journal.r-project.org/archive/2014-2/korkmaz-goksuluk-zararsiz.pdf>).

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
