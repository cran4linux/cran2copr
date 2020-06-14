%global packname  RcmdrPlugin.TeachStat
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          2%{?dist}
Summary:          RCommander Plugin for Teaching Statistical Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.3.0
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-randtests 
BuildRequires:    R-CRAN-tseries 
Requires:         R-CRAN-Rcmdr >= 2.3.0
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-randtests 
Requires:         R-CRAN-tseries 

%description
RCommander plugin for teaching statistical methods. It adds a new menu for
making easier the teaching of the main concepts about the main statistical
methods.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
