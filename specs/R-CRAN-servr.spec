%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  servr
%global packver   0.29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.29
Release:          1%{?dist}%{?buildtag}
Summary:          A Simple HTTP Server to Serve Static Files or Dynamic Documents

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httpuv >= 1.5.2
BuildRequires:    R-CRAN-xfun >= 0.42
BuildRequires:    R-CRAN-mime >= 0.2
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httpuv >= 1.5.2
Requires:         R-CRAN-xfun >= 0.42
Requires:         R-CRAN-mime >= 0.2
Requires:         R-CRAN-jsonlite 

%description
Start an HTTP server in R to serve static files, or dynamic documents that
can be converted to HTML files (e.g., R Markdown) under a given directory.

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
