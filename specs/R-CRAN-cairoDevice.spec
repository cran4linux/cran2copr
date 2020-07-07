%global packname  cairoDevice
%global packver   2.28
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.28
Release:          3%{?dist}
Summary:          Embeddable Cairo Graphics Device Driver

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cairo-devel >= 1.0
BuildRequires:    gtk2-devel
Requires:         cairo
Requires:         gtk2
BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildRequires:    R-grDevices 
Requires:         R-grDevices 

%description
This device uses Cairo and GTK to draw to the screen, file (png, svg, pdf,
and ps) or memory (arbitrary GdkDrawable or Cairo context). The screen
device may be embedded into RGtk2 interfaces and supports all interactive
features of other graphics devices, including getGraphicsEvent().

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
