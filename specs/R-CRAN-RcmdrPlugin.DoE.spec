%global __brp_check_rpaths %{nil}
%global packname  RcmdrPlugin.DoE
%global packver   0.12-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.3
Release:          3%{?dist}%{?buildtag}
Summary:          R Commander Plugin for (industrial) Design of Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FrF2 >= 1.2
BuildRequires:    R-CRAN-DoE.wrapper >= 0.8
BuildRequires:    R-CRAN-DoE.base >= 0.22.8
BuildRequires:    R-utils 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-relimp 
BuildRequires:    R-CRAN-Rcmdr 
BuildRequires:    R-CRAN-RcmdrMisc 
Requires:         R-CRAN-FrF2 >= 1.2
Requires:         R-CRAN-DoE.wrapper >= 0.8
Requires:         R-CRAN-DoE.base >= 0.22.8
Requires:         R-utils 
Requires:         R-tcltk 
Requires:         R-CRAN-relimp 
Requires:         R-CRAN-Rcmdr 
Requires:         R-CRAN-RcmdrMisc 

%description
The package provides a platform-independent GUI for design of experiments.
It is implemented as a plugin to the R-Commander, which is a more general
graphical user interface for statistics in R based on tcl/tk. DoE
functionality can be accessed through the menu Design that is added to the
R-Commander menus.

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
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/images
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
