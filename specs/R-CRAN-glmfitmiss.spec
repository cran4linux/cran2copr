%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmfitmiss
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting GLMs with Missing Data in Both Responses and Covariates

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.53
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-brglm2 >= 0.7.1
Requires:         R-CRAN-MASS >= 7.3.53
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-brglm2 >= 0.7.1

%description
Fits generalized linear models (GLMs) when there is missing data in both
the response and categorical covariates. The functions implement
likelihood-based methods using the Expectation and Maximization (EM)
algorithm and optionally apply Firth’s bias correction for improved
inference. See Pradhan, Nychka, and Bandyopadhyay (2025) <https:>, Maiti
and Pradhan (2009) <doi:10.1111/j.1541-0420.2008.01186.x>, Maity, Pradhan,
and Das (2019) <doi:10.1080/00031305.2017.1407359> for further
methodological details.

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
