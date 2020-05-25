%global debug_package %{nil}
%global packname  ROpenCVLite
%global packver   0.4.430
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.430
Release:          1%{?dist}
Summary:          Install 'OpenCV'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cmake
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-parallel 
Requires:         R-utils 
Requires:         R-CRAN-pkgbuild 
Requires:         R-parallel 

%description
Installs 'OpenCV' for use by other packages. 'OpenCV'
<https://opencv.org/> is library of programming functions mainly aimed at
real-time computer vision. This 'Lite' version contains the stable base
version of 'OpenCV' and does not contain any of its externally contributed
modules.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/OpenCVModule.4.3.0.cmake
%{rlibdir}/%{packname}/INDEX
