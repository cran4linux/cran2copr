%global packname  biplotbootGUI
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Bootstrap on Classical Biplots and Clustering Disjoint Biplot

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
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dendroextras 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-matlib 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-stats 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-utils 
Requires:         R-cluster 
Requires:         R-CRAN-dendroextras 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-CRAN-matlib 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-shapes 
Requires:         R-stats 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-tkrplot 
Requires:         R-utils 

%description
A GUI with which the user can construct and interact with Bootstrap
methods on Classical Biplots and with Clustering and/or Disjoint Biplot.
This GUI is also aimed for estimate any numerical data matrix using the
Clustering and Disjoint Principal component (CDPCA) methodology.

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
