%global packname  shiny
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Web Application Framework for R

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.0
BuildRequires:    R-CRAN-commonmark >= 1.7
BuildRequires:    R-CRAN-httpuv >= 1.5.2
BuildRequires:    R-CRAN-glue >= 1.3.2
BuildRequires:    R-CRAN-promises >= 1.1.0
BuildRequires:    R-CRAN-later >= 1.0.0
BuildRequires:    R-CRAN-fastmap >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.16
BuildRequires:    R-CRAN-htmltools >= 0.4.0.9003
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-mime >= 0.3
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-sourcetools 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-R6 >= 2.0
Requires:         R-CRAN-commonmark >= 1.7
Requires:         R-CRAN-httpuv >= 1.5.2
Requires:         R-CRAN-glue >= 1.3.2
Requires:         R-CRAN-promises >= 1.1.0
Requires:         R-CRAN-later >= 1.0.0
Requires:         R-CRAN-fastmap >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9.16
Requires:         R-CRAN-htmltools >= 0.4.0.9003
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-mime >= 0.3
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-sourcetools 
Requires:         R-tools 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-withr 

%description
Makes it incredibly easy to build interactive web applications with R.
Automatic "reactive" binding between inputs and outputs and extensive
prebuilt widgets make it possible to build beautiful, responsive, and
powerful applications with minimal effort.

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

%files
%{rlibdir}/%{packname}
