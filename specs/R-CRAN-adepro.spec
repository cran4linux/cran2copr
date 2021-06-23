%global __brp_check_rpaths %{nil}
%global packname  adepro
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          A 'shiny' Application for the (Audio-)Visualization of AdverseEvent Profiles

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-seriation 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-audio 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-gclus 
BuildRequires:    R-CRAN-TeachingDemos 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-seriation 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-V8 
Requires:         R-utils 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-audio 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-haven 
Requires:         R-stats 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-gclus 
Requires:         R-CRAN-TeachingDemos 

%description
Contains a 'shiny' application called AdEPro (Animation of Adverse Event
Profiles) which (audio-)visualizes adverse events occurring in clinical
trials. As this data is usually considered sensitive, this tool is
provided as a stand-alone application that can be launched from any local
machine on which the data is stored.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
