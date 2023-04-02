%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ezknitr
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Avoid the Typical Working Directory Pain When Using 'knitr'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.7
BuildRequires:    R-CRAN-R.utils >= 1.34.0
BuildRequires:    R-CRAN-markdown >= 0.7
Requires:         R-CRAN-knitr >= 1.7
Requires:         R-CRAN-R.utils >= 1.34.0
Requires:         R-CRAN-markdown >= 0.7

%description
An extension of 'knitr' that adds flexibility in several ways. One common
source of frustration with 'knitr' is that it assumes the directory where
the source file lives should be the working directory, which is often not
true. 'ezknitr' addresses this problem by giving you complete control over
where all the inputs and outputs are, and adds several other convenient
features to make rendering markdown/HTML documents easier.

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
