%global __brp_check_rpaths %{nil}
%global packname  acumos
%global packver   0.4-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          'Acumos' R Interface

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-RProtoBuf 
BuildRequires:    R-CRAN-Rserve 
BuildRequires:    R-CRAN-RestRserve 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-RProtoBuf 
Requires:         R-CRAN-Rserve 
Requires:         R-CRAN-RestRserve 
Requires:         R-CRAN-yaml 

%description
Create, upload and run 'Acumos' R models. 'Acumos'
(<https://www.acumos.org>) is a platform and open source framework
intended to make it easy to build, share, and deploy AI apps. 'Acumos' is
part of the 'LF AI Foundation', an umbrella organization within 'The Linux
Foundation'. With this package, user can create a component, and push it
to an 'Acumos' platform.

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
