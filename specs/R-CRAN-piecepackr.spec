%global packname  piecepackr
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Board Game Graphics

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         ghostscript
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridGeometry 
BuildRequires:    R-CRAN-grImport2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
Requires:         R-grid 
Requires:         R-CRAN-gridGeometry 
Requires:         R-CRAN-grImport2 
Requires:         R-grDevices 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-tools 

%description
Functions to make board game graphics.  By default makes game diagrams,
animations, and "Print & Play" layouts for the 'piecepack'
<http://www.ludism.org/ppwiki> but can be configured to make graphics for
other board game systems.

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
