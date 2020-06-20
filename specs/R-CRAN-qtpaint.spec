%global debug_package %{nil}
%global packname  qtpaint
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          Qt-Based Painting Infrastructure

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cmake
BuildRequires:    qt-devel
BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildRequires:    R-CRAN-qtbase >= 0.99.2
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-qtbase >= 0.99.2
Requires:         R-utils 
Requires:         R-methods 

%description
Low-level interface to functionality in Qt for efficiently drawing dynamic
graphics and handling basic user input.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
