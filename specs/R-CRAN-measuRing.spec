%global packname  measuRing
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Detection and Control of Tree-Ring Widths on Scanned ImageSections

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pastecs 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-dplR 
Requires:         R-CRAN-pastecs 
Requires:         R-CRAN-png 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-dplR 

%description
Identification of ring borders on scanned image sections from
dendrochronological samples. Processing of image reflectances to produce
gray matrices and time series of smoothed gray values. Luminance data is
plotted on segmented images for users to perform both: visual
identification of ring borders or control of automatic detection. Routines
to visually include/exclude ring borders on the R graphical devices, or
automatically detect ring borders using a linear detection algorithm. This
algorithm detects ring borders according to positive/negative extreme
values in the smoothed time-series of gray values. Most of the in-package
routines can be recursively implemented using the multiDetect() function.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/P105_a.png
%doc %{rlibdir}/%{packname}/P105_a.tif
%doc %{rlibdir}/%{packname}/P105_b.tif
%doc %{rlibdir}/%{packname}/P105_c.tif
%doc %{rlibdir}/%{packname}/P105_d.tif
%{rlibdir}/%{packname}/INDEX
