%global packname  svDialogs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          'SciViews' - Standard Dialog Boxes for Windows, MacOS andLinuxes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         zenity
Requires:         yad
BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-svGUI >= 1.0.0
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-svGUI >= 1.0.0
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-utils 
Requires:         R-methods 

%description
Rapidly construct standard dialog boxes for your GUI, including message
boxes, input boxes, list, file or directory selection, ... In case R
cannot display GUI dialog boxes, a simpler command line version of these
interactive elements is also provided as fallback solution.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gui
%{rlibdir}/%{packname}/INDEX
