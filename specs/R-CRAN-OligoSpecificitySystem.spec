%global packname  OligoSpecificitySystem
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}
Summary:          Oligo Specificity System

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
Requires:         tcl
Requires:         tk
Requires:         bwidget
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 

%description
Calculate the theorical specificity of a system of multiple primers used
for PCR, qPCR primers or degenerated primer design

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Rlogo.gif
%doc %{rlibdir}/%{packname}/tcltk.gif
%doc %{rlibdir}/%{packname}/Thumbs.db
%{rlibdir}/%{packname}/INDEX
