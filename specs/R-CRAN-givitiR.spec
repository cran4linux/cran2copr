%global packname  givitiR
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          The GiViTI Calibration Test and Belt

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-rootSolve 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Functions to assess the calibration of logistic regression models with the
GiViTI (Gruppo Italiano per la Valutazione degli interventi in Terapia
Intensiva, Italian Group for the Evaluation of the Interventions in
Intensive Care Units - see <http://www.giviti.marionegri.it/>) approach.
The approach consists in a graphical tool, namely the GiViTI calibration
belt, and in the associated statistical test. These tools can be used both
to evaluate the internal calibration (i.e. the goodness of fit) and to
assess the validity of an externally developed model.

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
%{rlibdir}/%{packname}/INDEX
