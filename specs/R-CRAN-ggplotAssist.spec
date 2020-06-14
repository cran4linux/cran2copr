%global packname  ggplotAssist
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          'RStudio' Addin for Teaching and Learning 'ggplot2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi >= 0.5
BuildRequires:    R-CRAN-shiny >= 0.13
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-gcookbook 
BuildRequires:    R-CRAN-moonBook 
BuildRequires:    R-CRAN-editData 
Requires:         R-CRAN-rstudioapi >= 0.5
Requires:         R-CRAN-shiny >= 0.13
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-gcookbook 
Requires:         R-CRAN-moonBook 
Requires:         R-CRAN-editData 

%description
An 'RStudio' addin for teaching and learning making plot using the
'ggplot2' package. You can learn each steps of making plot by clicking
your mouse without coding. You can get resultant code for the plot.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/textFunctionExample
%doc %{rlibdir}/%{packname}/textFunctionExample2
%{rlibdir}/%{packname}/INDEX
