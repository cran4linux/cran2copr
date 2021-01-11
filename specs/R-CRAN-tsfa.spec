%global packname  tsfa
%global packver   2021.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2021.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Factor Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tfplot >= 2014.2.1
BuildRequires:    R-CRAN-tframe >= 2011.3.1
BuildRequires:    R-CRAN-GPArotation >= 2006.9.1
BuildRequires:    R-CRAN-dse >= 2006.1.1
BuildRequires:    R-CRAN-EvalEst >= 2006.1.1
BuildRequires:    R-CRAN-setRNG >= 2004.4.1
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-tfplot >= 2014.2.1
Requires:         R-CRAN-tframe >= 2011.3.1
Requires:         R-CRAN-GPArotation >= 2006.9.1
Requires:         R-CRAN-dse >= 2006.1.1
Requires:         R-CRAN-EvalEst >= 2006.1.1
Requires:         R-CRAN-setRNG >= 2004.4.1
Requires:         R-stats 
Requires:         R-graphics 

%description
Extraction of Factors from Multivariate Time Series. See '?00tsfa-Intro'
for more details.

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
