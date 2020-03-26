%global packname  radiant.multivariate
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}
Summary:          Multivariate Menu for Radiant: Business Analytics using R andShiny

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-CRAN-GPArotation >= 2014.11.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-car >= 2.1.1
BuildRequires:    R-CRAN-psych >= 1.8.4
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-radiant.data >= 1.3.0
BuildRequires:    R-CRAN-radiant.model >= 1.3.0
BuildRequires:    R-CRAN-import >= 1.1.0
BuildRequires:    R-CRAN-patchwork >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-ggrepel >= 0.8
BuildRequires:    R-CRAN-polycor >= 0.7.10
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-scales >= 0.4.0
BuildRequires:    R-CRAN-gower >= 0.2.1
BuildRequires:    R-CRAN-clustMixType >= 0.2.1
Requires:         R-MASS >= 7.3
Requires:         R-CRAN-GPArotation >= 2014.11.1
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-car >= 2.1.1
Requires:         R-CRAN-psych >= 1.8.4
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-radiant.data >= 1.3.0
Requires:         R-CRAN-radiant.model >= 1.3.0
Requires:         R-CRAN-import >= 1.1.0
Requires:         R-CRAN-patchwork >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-ggrepel >= 0.8
Requires:         R-CRAN-polycor >= 0.7.10
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-scales >= 0.4.0
Requires:         R-CRAN-gower >= 0.2.1
Requires:         R-CRAN-clustMixType >= 0.2.1

%description
The Radiant Multivariate menu includes interfaces for perceptual mapping,
factor analysis, cluster analysis, and conjoint analysis. The application
extends the functionality in radiant.data.

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
%doc %{rlibdir}/%{packname}/app
%{rlibdir}/%{packname}/INDEX
