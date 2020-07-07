%global packname  xpose
%global packver   0.4.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.10
Release:          3%{?dist}
Summary:          Diagnostics for Pharmacometric Models

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-tibble >= 2.1.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.0
BuildRequires:    R-CRAN-vpc >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-tidyr >= 0.8.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-ggforce >= 0.2.0
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-tibble >= 2.1.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.0
Requires:         R-CRAN-vpc >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-tidyr >= 0.8.0
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-ggforce >= 0.2.0
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-stats 

%description
Diagnostics for non-linear mixed-effects (population) models from 'NONMEM'
<https://www.iconplc.com/innovation/nonmem/>. 'xpose' facilitates data
import, creation of numerical run summary and provide 'ggplot2'-based
graphics for data exploration and model diagnostics.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
