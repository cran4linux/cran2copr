%global packname  parcats
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Interactive Parallel Categories Diagrams for 'easyalluvial'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-easyalluvial >= 0.2.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-easyalluvial >= 0.2.1.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-stringr 

%description
Complex graphical representations of data are best explored using
interactive elements. 'parcats' adds interactive graphing capabilities to
the 'easyalluvial' package. The 'plotly.js' parallel categories diagrams
offer a good framework for creating interactive flow graphs that allow
manual drag and drop sorting of dimensions and categories, highlighting
single flows and displaying mouse over information. The 'plotly.js'
dependency is quite heavy and therefore is outsourced into a separate
package.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/htmlwidgetsgist.R
%doc %{rlibdir}/%{packname}/logo
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
