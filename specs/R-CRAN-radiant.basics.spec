%global packname  radiant.basics
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Basics Menu for Radiant: Business Analytics using R and Shiny

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-psych >= 1.8.3.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.2.0
BuildRequires:    R-CRAN-import >= 1.1.0
BuildRequires:    R-CRAN-radiant.data >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-scales >= 0.4.0
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-psych >= 1.8.3.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shiny >= 1.2.0
Requires:         R-CRAN-import >= 1.1.0
Requires:         R-CRAN-radiant.data >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-scales >= 0.4.0

%description
The Radiant Basics menu includes interfaces for probability calculation,
central limit theorem simulation, comparing means and proportions,
goodness-of-fit testing, cross-tabs, and correlation. The application
extends the functionality in radiant.data.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/app
%{rlibdir}/%{packname}/INDEX
