%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rafsi
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Ranking of Alternatives with the RAFSI Method

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch

%description
Ranking of Alternatives through Functional mapping of criterion
sub-intervals into a Single Interval Method is designed to perform
multi-criteria decision-making (MCDM), developed by Mališa Žižovic in 2020
(<doi:10.3390/math8061015>). It calculates the final sorted rankings based
on a decision matrix where rows represent alternatives and columns
represent criteria. The method uses: - A numeric vector of weights for
each criterion (the sum of weights must be 1). - A numeric vector of ideal
values for each criterion. - A numeric vector of anti-ideal values for
each criterion. - Numeric values representing the extent to which the
ideal value is preferred over the anti-ideal value, and the extent to
which the anti-ideal value is considered worse. The function standardizes
the decision matrix, normalizes the data, applies weights, and returns the
final sorted rankings.

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
