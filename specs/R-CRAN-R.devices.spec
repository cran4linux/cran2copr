%global packname  R.devices
%global packver   2.16.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.16.1
Release:          1%{?dist}
Summary:          Unified Handling of Graphics Devices

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.6.0
BuildRequires:    R-CRAN-R.methodsS3 >= 1.7.1
BuildRequires:    R-CRAN-R.oo >= 1.21.0
BuildRequires:    R-CRAN-base64enc >= 0.1.2
BuildRequires:    R-grDevices 
Requires:         R-CRAN-R.utils >= 2.6.0
Requires:         R-CRAN-R.methodsS3 >= 1.7.1
Requires:         R-CRAN-R.oo >= 1.21.0
Requires:         R-CRAN-base64enc >= 0.1.2
Requires:         R-grDevices 

%description
Functions for creating plots and image files in a unified way regardless
of output format (EPS, PDF, PNG, SVG, TIFF, WMF, etc.). Default device
options as well as scales and aspect ratios are controlled in a uniform
way across all device types. Switching output format requires minimal
changes in code. This package is ideal for large-scale batch processing,
because it will never leave open graphics devices or incomplete image
files behind, even on errors or user interrupts.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/exdata
%{rlibdir}/%{packname}/INDEX
