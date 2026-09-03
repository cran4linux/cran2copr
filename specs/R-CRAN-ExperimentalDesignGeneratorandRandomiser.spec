%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ExperimentalDesignGeneratorandRandomiser
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'EDGAR': Experimental Design Generator and Randomiser

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch

%description
Native R implementation of 'EDGAR', the Experimental Design Generator and
Randomiser. 'EDGAR' was originally developed as a suite of 'Excel'
<https://www.microsoft.com/microsoft-365/excel> workbooks by the
Biometrics team at Rothamsted Research <http://www.edgarweb.org.uk/>. The
algorithms were subsequently re-implemented in the open-source 'Python'
<https://www.python.org/> project 'rotsl/edgar'
<https://rotsl.github.io/edgar/>, distributed as the 'edgar-design'
package on 'PyPI' <https://pypi.org/project/edgar-design/>. This R package
is a native R port of that 'Python' implementation: it does not require
'Python', 'reticulate' <https://CRAN.R-project.org/package=reticulate>, or
any external service at runtime, and provides deterministic, reproducible
randomisation for nine experimental designs including alpha designs
(Patterson and Williams, 1976) <doi:10.1093/biomet/63.1.83>.
Cross-language reproducibility with the 'Python' implementation is
achieved by porting the Mersenne Twister seeding implementation from
'CPython' <https://github.com/python/cpython> and the Fisher-Yates shuffle
to native R.

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
