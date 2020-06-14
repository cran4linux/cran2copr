%global packname  ade4TkGUI
%global packver   0.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}
Summary:          'ade4' Tcl/Tk Graphical User Interface

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 >= 1.4.3
BuildRequires:    R-CRAN-adegraphics 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-utils 
Requires:         R-CRAN-ade4 >= 1.4.3
Requires:         R-CRAN-adegraphics 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 
Requires:         R-utils 

%description
A Tcl/Tk GUI for some basic functions in the 'ade4' package.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/Rlogo.gif
%doc %{rlibdir}/%{packname}/tcltk.gif
%{rlibdir}/%{packname}/INDEX
