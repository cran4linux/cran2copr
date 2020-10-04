%global packname  RGtk2
%global packver   2.20.36
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.20.36
Release:          3%{?dist}%{?buildtag}
Summary:          R Bindings for Gtk 2.8.0 and Above

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cairo-devel >= 1.0.0
BuildRequires:    atk-devel >= 1.10.0
BuildRequires:    pango-devel >= 1.10.0
BuildRequires:    gtk2-devel >= 2.8.0
BuildRequires:    glib2-devel >= 2.8.0
Requires:         cairo
Requires:         atk
Requires:         pango
Requires:         gtk2
Requires:         glib2
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Facilities in the R language for programming graphical interfaces using
Gtk, the Gimp Tool Kit.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/ui
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
