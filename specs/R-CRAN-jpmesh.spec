%global packname  jpmesh
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Utilities for Japanese Mesh Code

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-leaflet >= 1.1.0
BuildRequires:    R-CRAN-shiny >= 1.0.5
BuildRequires:    R-CRAN-sf >= 0.5.5
BuildRequires:    R-CRAN-units >= 0.5.1
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-rlang >= 0.1.4
BuildRequires:    R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-leaflet >= 1.1.0
Requires:         R-CRAN-shiny >= 1.0.5
Requires:         R-CRAN-sf >= 0.5.5
Requires:         R-CRAN-units >= 0.5.1
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-rlang >= 0.1.4
Requires:         R-CRAN-miniUI >= 0.1.1

%description
Helpful functions for using mesh code (80km to 125m) data in Japan.
Visualize mesh code using 'ggplot2' and 'leaflet', etc.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
