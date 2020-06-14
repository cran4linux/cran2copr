%global packname  LAGOSNE
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          2%{?dist}
Summary:          Interface to the Lake Multi-Scaled Geospatial and TemporalDatabase

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.7.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-CRAN-purrr >= 0.2.2.2
BuildRequires:    R-CRAN-lazyeval >= 0.2
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-curl >= 2.7.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-purrr >= 0.2.2.2
Requires:         R-CRAN-lazyeval >= 0.2
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-progress 

%description
Client for programmatic access to the Lake Multi-scaled Geospatial and
Temporal database <https://lagoslakes.org>, with functions for accessing
lake water quality and ecological context data for the US.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gh-card.png
%doc %{rlibdir}/%{packname}/lagos_banner.png
%doc %{rlibdir}/%{packname}/lagos_banner2.png
%doc %{rlibdir}/%{packname}/lagos_hex.png
%doc %{rlibdir}/%{packname}/lagos_test_subset.rds
%doc %{rlibdir}/%{packname}/lagos-transparent.png
%doc %{rlibdir}/%{packname}/lagos.png
%{rlibdir}/%{packname}/INDEX
