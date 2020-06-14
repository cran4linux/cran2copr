%global packname  bulletcp
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Automatic Groove Identification via Bayesian ChangepointDetection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-Rdpack 

%description
Provides functionality to automatically detect groove locations via a
Bayesian changepoint detection method to be used in the data preprocessing
step of forensic bullet matching algorithms. The methods in this package
are based on those in Stephens (1994) <doi:10.2307/2986119>. Bayesian
changepoint detection will simply be an option in the function from the
package 'bulletxtrctr' which identifies the groove locations.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/REFERENCES.bib.sav
%{rlibdir}/%{packname}/INDEX
