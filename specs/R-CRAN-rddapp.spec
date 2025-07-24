%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rddapp
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Discontinuity Design Application

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.6.0
BuildRequires:    R-CRAN-sandwich >= 2.3.4
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-AER >= 1.2.5
BuildRequires:    R-CRAN-Formula >= 1.2.1
BuildRequires:    R-CRAN-plot3D >= 1.1.1
BuildRequires:    R-CRAN-lmtest >= 0.9.35
BuildRequires:    R-CRAN-DT >= 0.2
BuildRequires:    R-CRAN-shiny >= 0.14
Requires:         R-CRAN-R.utils >= 2.6.0
Requires:         R-CRAN-sandwich >= 2.3.4
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-AER >= 1.2.5
Requires:         R-CRAN-Formula >= 1.2.1
Requires:         R-CRAN-plot3D >= 1.1.1
Requires:         R-CRAN-lmtest >= 0.9.35
Requires:         R-CRAN-DT >= 0.2
Requires:         R-CRAN-shiny >= 0.14

%description
Estimation of both single- and multiple-assignment Regression
Discontinuity Designs (RDDs). Provides both parametric (global) and
non-parametric (local) estimation choices for both sharp and fuzzy
designs, along with power analysis and assumption checks. Introductions to
the underlying logic and analysis of RDDs are in Thistlethwaite, D. L.,
Campbell, D. T. (1960) <doi:10.1037/h0044319> and Lee, D. S., Lemieux, T.
(2010) <doi:10.1257/jel.48.2.281>.

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
