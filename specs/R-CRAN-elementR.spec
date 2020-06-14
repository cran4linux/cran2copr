%global packname  elementR
%global packver   1.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          2%{?dist}
Summary:          An Framework for Reducing Elemental LAICPMS Data from SolidStructures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-gnumeric 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-reader 
BuildRequires:    R-CRAN-readODS 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-outliers 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httpuv 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-gnumeric 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lmtest 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-reader 
Requires:         R-CRAN-readODS 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-outliers 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-colourpicker 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-httpuv 

%description
Aims to facilitate the reduction of elemental microchemistry data from
solid-phase LAICPMS analysis (laser ablation inductive coupled plasma mass
spectrometry). The 'elementR' package provides a reactive and user
friendly interface (based on a 'shiny' application) and a set of 'R6'
classes for conducting all steps needed for an optimal data reduction
while leaving maximum control for user.

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
%doc %{rlibdir}/%{packname}/AtomicMass.csv
%doc %{rlibdir}/%{packname}/elementR_documentation.pdf
%doc %{rlibdir}/%{packname}/Example_conversion
%doc %{rlibdir}/%{packname}/Example_Session
%doc %{rlibdir}/%{packname}/Results
%doc %{rlibdir}/%{packname}/splitReplicate_example.csv
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
