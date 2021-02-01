%global packname  betafunctions
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Working with Two- And Four-Parameter Beta Probability Distributions

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Package providing a number of functions for working with Two- and
Four-parameter Beta distributions, including alternative
parameterizations, calculation of moments, and fitting of Beta
distributions to vectors of values. Also includes functions for estimating
classification accuracy, diagnostic performance and consistency, using
what is generally known as the "Livingston and Lewis approach" in the
psychometric literature as the foundational method, which makes extensive
use of the Beta distribution. A shiny application is now online, providing
a GUI for the Livingston and Lewis approach. See documentation for LL.CA()
function. Livingston and Lewis (1995)
<doi:10.1111/j.1745-3984.1995.tb00462.x>. Hanson (1991)
<https://files.eric.ed.gov/fulltext/ED344945.pdf>. Glas, Lijmer, Prins,
Bonsel and Bossuyt (2003) <doi:10.1016/S0895-4356(03)00177-X>.

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
