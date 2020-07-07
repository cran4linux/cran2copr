%global packname  questionr
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          3%{?dist}
Summary:          Functions to Make Surveys Processing Easier

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         xclip
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-labelled >= 2.4.0
BuildRequires:    R-CRAN-haven >= 2.3.0
BuildRequires:    R-CRAN-shiny >= 1.0.5
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-highr 
BuildRequires:    R-CRAN-styler 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-labelled >= 2.4.0
Requires:         R-CRAN-haven >= 2.3.0
Requires:         R-CRAN-shiny >= 1.0.5
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-highr 
Requires:         R-CRAN-styler 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-htmltools 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Set of functions to make the processing and analysis of surveys easier :
interactive shiny apps and addins for data recoding, contingency tables,
dataset metadata handling, and several convenience functions.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/po
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
