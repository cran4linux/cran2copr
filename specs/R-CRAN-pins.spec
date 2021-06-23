%global __brp_check_rpaths %{nil}
%global packname  pins
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Pin, Discover and Share Resources

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-backports 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-filelock 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-rappdirs 
Requires:         R-stats 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-zip 

%description
Pin remote resources into a local cache to work offline, improve speed and
avoid recomputing; discover and share resources in local folders,
'GitHub', 'Kaggle' or 'RStudio Connect'. Resources can be anything from
'CSV', 'JSON', or image files to arbitrary R objects.

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
