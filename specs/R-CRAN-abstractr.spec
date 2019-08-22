%global packname  abstractr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          An R-Shiny Application for Creating Visual Abstracts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-shiny >= 1.2.0
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-emojifont 
BuildRequires:    R-CRAN-rintrojs 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-shiny >= 1.2.0
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-emojifont 
Requires:         R-CRAN-rintrojs 

%description
An R-Shiny application to create visual abstracts for original research. A
variety of user defined options and formatting are included.

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
%doc %{rlibdir}/%{packname}/abstractR
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
