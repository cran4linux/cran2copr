%global packname  ICSsmoothing
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Data Smoothing by Interpolating Cubic Splines

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-ggplot2 

%description
We construct the explicit form of clamped cubic interpolating spline (both
uniform - knots are equidistant and non-uniform - knots are arbitrary).
Using this form, we propose a linear regression model suitable for real
data smoothing. This package is based on a diploma thesis Hudak (2017)
<https://opac.crzp.sk/?fn=detailBiblioForm&sid=7FE4E0810F66E41DF9A9CA23557F&seo=CRZP-detail-kniha>.

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
