%global packname  adepro
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          A 'shiny' Application for the (Audio-)Visualization of AdverseEvent Profiles

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-audio 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-MASS 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-graphics 
Requires:         R-CRAN-audio 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-Cairo 
Requires:         R-MASS 

%description
Contains a 'shiny' application called AdEPro (Animation of Adverse Event
Profiles) which (audio-)visualizes adverse events occurring in clinical
trials. As this data is usually considered sensitive, this tool is
provided as a stand-alone application that can be launched from any local
machine on which the data is stored.

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
