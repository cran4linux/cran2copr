%global __brp_check_rpaths %{nil}
%global packname  gimmeTools
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Supplemental Tools for the 'gimme' R Package

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-easycsv 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-easycsv 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-magrittr 

%description
Supplemental tools for the 'gimme' R package. It contains an interactive
graphical user interface, allowing for the flexible specification of a
variety of both basic and advanced options. It will expand to include a
variety of tools for navigating output.

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
