%global packname  temperatureresponse
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          2%{?dist}
Summary:          Temperature Response

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-AICcmodavg 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-AICcmodavg 
Requires:         R-CRAN-numDeriv 

%description
Fits temperature response models to rate measurements taken at different
temperatures. Etienne Low-Decarie,Tobias G. Boatman, Noah Bennett,Will
Passfield,Antonio Gavalas-Olea,Philipp Siegel, Richard J. Geider (2017)
<doi:10.1002/ece3.3576> .

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
