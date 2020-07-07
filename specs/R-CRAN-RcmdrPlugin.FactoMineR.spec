%global packname  RcmdrPlugin.FactoMineR
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          3%{?dist}
Summary:          Graphical User Interface for FactoMineR

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.0.0
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-Rcmdr >= 2.0.0
Requires:         R-CRAN-FactoMineR 
Requires:         R-tcltk 

%description
Rcmdr Plugin for the 'FactoMineR' package.

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
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
