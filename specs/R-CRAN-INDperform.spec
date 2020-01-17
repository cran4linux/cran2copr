%global packname  INDperform
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Evaluation of Indicator Performances for Assessing EcosystemStates

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grDevices >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-nlme >= 3.1.137
BuildRequires:    R-CRAN-vegan >= 2.5.6
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-mgcv >= 1.8.26
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-htmlwidgets >= 1.5.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-cowplot >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-rlang >= 0.4.2
BuildRequires:    R-CRAN-rhandsontable >= 0.3.7
BuildRequires:    R-CRAN-purrr >= 0.3.3
Requires:         R-grDevices >= 3.5.0
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-nlme >= 3.1.137
Requires:         R-CRAN-vegan >= 2.5.6
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-mgcv >= 1.8.26
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-htmlwidgets >= 1.5.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-cowplot >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-rlang >= 0.4.2
Requires:         R-CRAN-rhandsontable >= 0.3.7
Requires:         R-CRAN-purrr >= 0.3.3

%description
An implementation of the 7-step approach suggested by Otto et al. (2018)
<doi:10.1016/j.ecolind.2017.05.045> to validate ecological state
indicators and to select a suite of complimentary and well performing
indicators. This suite can be then used to assess the current state of the
system in comparison to a reference period. However, the tools in this
package are very generic and can be used to test any type of indicator
(e.g. social or economic indicators).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
