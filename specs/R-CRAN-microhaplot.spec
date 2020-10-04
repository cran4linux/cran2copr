%global packname  microhaplot
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Microhaplotype Constructor and Visualizer

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.5.0
BuildRequires:    R-grid >= 3.1.2
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shinyBS >= 0.61
BuildRequires:    R-CRAN-ggiraph >= 0.6.0
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-shinyWidgets >= 0.4.3
BuildRequires:    R-CRAN-tidyr >= 0.4.1
BuildRequires:    R-CRAN-scales >= 0.4.0
BuildRequires:    R-CRAN-shiny >= 0.13.2
BuildRequires:    R-CRAN-DT >= 0.1
Requires:         R-CRAN-gtools >= 3.5.0
Requires:         R-grid >= 3.1.2
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shinyBS >= 0.61
Requires:         R-CRAN-ggiraph >= 0.6.0
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-shinyWidgets >= 0.4.3
Requires:         R-CRAN-tidyr >= 0.4.1
Requires:         R-CRAN-scales >= 0.4.0
Requires:         R-CRAN-shiny >= 0.13.2
Requires:         R-CRAN-DT >= 0.1

%description
A downstream bioinformatics tool to construct and assist curation of
microhaplotypes from short read sequences.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/perl
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
