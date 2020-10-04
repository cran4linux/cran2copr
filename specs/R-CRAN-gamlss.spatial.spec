%global packname  gamlss.spatial
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial Terms in Generalized Additive Models for Location Scaleand Shape Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss >= 4.2.7
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-gamlss.add 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
Requires:         R-CRAN-gamlss >= 4.2.7
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-gamlss.add 
Requires:         R-CRAN-spam 
Requires:         R-mgcv 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 

%description
It allows us to fit Gaussian Markov Random Field within the Generalized
Additive Models for Location Scale and Shape algorithms.

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
