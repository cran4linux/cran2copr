%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyfst
%global packver   1.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Verbs for Fast Data Manipulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-fst >= 0.9.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-fst >= 0.9.0

%description
A toolkit of tidy data manipulation verbs with 'data.table' as the
backend. Combining the merits of syntax elegance from 'dplyr' and
computing performance from 'data.table', 'tidyfst' intends to provide
users with state-of-the-art data manipulation tools with least pain. This
package is an extension of 'data.table'. While enjoying a tidy syntax, it
also wraps combinations of efficient functions to facilitate
frequently-used data operations.

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
