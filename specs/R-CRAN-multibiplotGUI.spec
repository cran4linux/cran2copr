%global packname  multibiplotGUI
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Multibiplot Analysis in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
Requires:         tcl
Requires:         tk
Requires:         bwidget
BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dendroextras 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-tkrplot 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-shapes 
Requires:         R-cluster 
Requires:         R-CRAN-dendroextras 
Requires:         R-Matrix 

%description
A GUI with which users can construct and interact with Multibiplot
Analysis and provides inferential results by using Bootstrap Methods.

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
%{rlibdir}/%{packname}/INDEX
