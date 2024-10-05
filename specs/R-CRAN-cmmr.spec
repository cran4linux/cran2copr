%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cmmr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          CEU Mass Mediator RESTful API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-cli 

%description
CEU (CEU San Pablo University) Mass Mediator is an on-line tool for aiding
researchers in performing metabolite annotation. 'cmmr' (CEU Mass Mediator
RESTful API) allows for programmatic access in R: batch search, batch
advanced search, MS/MS (tandem mass spectrometry) search, etc. For more
information about the API Endpoint please go to
<https://github.com/YaoxiangLi/cmmr>.

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
