%global packname  ggedit
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          Interactive 'ggplot2' Layer and Theme Aesthetic Editor

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-colourpicker >= 0.2
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-colourpicker >= 0.2
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-tools 
Requires:         R-stats 

%description
Interactively edit 'ggplot2' layer and theme aesthetics definitions.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
