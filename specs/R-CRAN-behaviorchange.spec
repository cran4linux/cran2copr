%global packname  behaviorchange
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Tools for Behavior Change Researchers and Professionals

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-BiasedUrn >= 1.07
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-data.tree >= 0.7.5
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-ufs >= 0.3.1
BuildRequires:    R-CRAN-googlesheets >= 0.3.0
BuildRequires:    R-CRAN-gtable >= 0.2.0
BuildRequires:    R-CRAN-magrittr >= 0.1
BuildRequires:    R-CRAN-DiagrammeRsvg >= 0.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-BiasedUrn >= 1.07
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-data.tree >= 0.7.5
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-CRAN-ufs >= 0.3.1
Requires:         R-CRAN-googlesheets >= 0.3.0
Requires:         R-CRAN-gtable >= 0.2.0
Requires:         R-CRAN-magrittr >= 0.1
Requires:         R-CRAN-DiagrammeRsvg >= 0.1

%description
Contains specialised analyses and visualisation tools for behavior change
science. These facilitate conducting determinant studies (for example,
using confidence interval-based estimation of relevance, CIBER, or
CIBERlite plots), systematically developing, reporting, and analysing
interventions (for example, using acyclic behavior change diagrams), and
reporting about intervention effectiveness (for example, using the Numbers
Needed for Change), and computing the required sample size (using the
Meaningful Change Definition). This package is especially useful for
researchers in the field of behavior change or health psychology and to
behavior change professionals such as intervention developers and
prevention workers.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
