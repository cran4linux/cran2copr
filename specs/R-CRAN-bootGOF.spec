%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bootGOF
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap Based Goodness-of-Fit Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-checkmate >= 2.0.0

%description
Bootstrap based goodness-of-fit tests. It allows to perform rigorous
statistical tests to check if a chosen model family is correct based on
the marked empirical process. The implemented algorithms are described in
(Dikta and Scheer (2021) <doi:10.1007/978-3-030-73480-0>) and can be
applied to generalized linear models without any further implementation
effort. As far as certain linearity conditions are fulfilled the
resampling scheme are also applicable beyond generalized linear models.
This is reflected in the software architecture which allows to reuse the
resampling scheme by implementing only certain interfaces for models that
are not supported natively by the package.

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
