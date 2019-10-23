%global packname  CONS
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Consonance Analysis Module

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
Requires:         tcl
Requires:         tk
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-gWidgets 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-REdaS 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-tcltk 
Requires:         R-CRAN-gWidgets 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-REdaS 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-gridExtra 

%description
Consonance Analysis is a useful numerical and graphical approach for
evaluating the consistency of the measurements and the panel of people
involved in sensory evaluation. It makes use of several uni and
multivariate techniques either graphical or analytical. It shows the
implementation of this procedure in a graphical interface.

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
