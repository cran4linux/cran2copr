%global packname  csurvey
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Regression for Survey Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.4
BuildRequires:    R-CRAN-survey >= 3.36
BuildRequires:    R-CRAN-Matrix >= 1.2.17
BuildRequires:    R-CRAN-coneproj >= 1.14
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-MASS >= 7.3.51.4
Requires:         R-CRAN-survey >= 3.36
Requires:         R-CRAN-Matrix >= 1.2.17
Requires:         R-CRAN-coneproj >= 1.14
Requires:         R-CRAN-purrr >= 0.3.4

%description
Domain mean estimation with monotonicity or block monotone constraints.
See Wu J, Meyer MC and Opsomer JD (2016)<doi:10.1002/cjs.11301> for more
details.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
