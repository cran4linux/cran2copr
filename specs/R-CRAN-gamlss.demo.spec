%global packname  gamlss.demo
%global packver   4.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Demos for GAMLSS

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rpanel >= 1.1.1
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-gamlss.tr 
BuildRequires:    R-tcltk 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-rpanel >= 1.1.1
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-gamlss.tr 
Requires:         R-tcltk 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Demos for smoothing and gamlss.family distributions.

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
