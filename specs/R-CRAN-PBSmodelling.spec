%global packname  PBSmodelling
%global packver   2.68.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.68.8
Release:          3%{?dist}%{?buildtag}
Summary:          GUI Tools Made Easy: Interact with Models and Explore Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
Requires:         bwidget
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-XML 
Requires:         R-methods 
Requires:         R-tcltk 
Requires:         R-CRAN-XML 

%description
Provides software to facilitate the design, testing, and operation of
computer models. It focuses particularly on tools that make it easy to
construct and edit a customized graphical user interface ('GUI'). Although
our simplified 'GUI' language depends heavily on the R interface to the
'Tcl/Tk' package, a user does not need to know 'Tcl/Tk'. Examples
illustrate models built with other R packages, including 'PBSmapping',
'PBSddesolve', and 'BRugs'. A complete user's guide 'PBSmodelling-UG.pdf'
shows how to use this package effectively.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/PBStools
%doc %{rlibdir}/%{packname}/tcl_scripts
%doc %{rlibdir}/%{packname}/testWidgets
%doc %{rlibdir}/%{packname}/thirdparty
%doc %{rlibdir}/%{packname}/unitTests
%doc %{rlibdir}/%{packname}/win
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
