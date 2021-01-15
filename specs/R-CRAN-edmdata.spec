%global packname  edmdata
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Sets for Psychometric Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Collection of data sets from various assessments that can be used to
evaluate psychometric models. These data sets have been analyzed in the
following papers that introduced new methodology as part of the
application section: Chen, Y., Culpepper, S. A., & Liang, F. (2020)
<doi:10.1007/s11336-019-09693-2> Culpepper, S. A. (2019a)
<doi:10.1007/s11336-019-09683-4>, Culpepper, S. A. (2019b)
<doi:10.1007/s11336-018-9643-8>, Culpepper, S. A., & Chen, Y. (2019)
<doi:10.3102/1076998618791306>, Culpepper, S. A., & Balamuta, J. J. (2017)
<doi:10.1007/s11336-015-9484-7>, and Culpepper, S. A. (2015)
<doi:10.3102/1076998615595403>.

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
