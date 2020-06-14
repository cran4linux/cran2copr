%global packname  rriskDistributions
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          2%{?dist}
Summary:          Fitting Distributions to Given Data or Known Quantiles

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

Requires:         tcl >= 8.5
Requires:         tk >= 8.5
BuildRequires:    R-devel >= 2.11.0
Requires:         R-core >= 2.11.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mc2d 
BuildRequires:    R-CRAN-eha 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mc2d 
Requires:         R-CRAN-eha 
Requires:         R-CRAN-msm 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 

%description
Collection of functions for fitting distributions to given data or by
known quantiles. Two main functions fit.perc() and fit.cont() provide
users a GUI that allows to choose a most appropriate distribution without
any knowledge of the R syntax. Note, this package is a part of the 'rrisk'
project.

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
%{rlibdir}/%{packname}/INDEX
