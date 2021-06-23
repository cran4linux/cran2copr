%global __brp_check_rpaths %{nil}
%global packname  gamlss.tr
%global packver   5.1-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Generating and Fitting Truncated `gamlss.family' Distributions

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.1
Requires:         R-core >= 2.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss >= 5.0.0
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-methods 
Requires:         R-CRAN-gamlss >= 5.0.0
Requires:         R-CRAN-gamlss.dist 
Requires:         R-methods 

%description
This is an add on package to GAMLSS. The purpose of this package is to
allow users to defined truncated distributions in GAMLSS models. The main
function gen.trun() generates truncated version of an existing GAMLSS
family distribution.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
