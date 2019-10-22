%global packname  HBV.IANIGLA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Decoupled Hydrological Model for Research and Education Purposes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-Rcpp >= 0.12.0

%description
The HBV (Hydrologiska Byråns Vattenbalansavdelning) hydrological model is
decoupled to allow the user to build his/her own model. This version was
developed by the author in IANIGLA-CONICET (Instituto Argentino de
Nivologia, Glaciologia y Ciencias Ambientales - Consejo Nacional de
Investigaciones Cientificas y Tecnicas) for hydroclimatic studies in the
Andes. HBV.IANIGLA incorporates modules for precipitation and temperature
interpolation, and also for clean and debris covered ice melt estimations.

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
%{rlibdir}/%{packname}/libs
