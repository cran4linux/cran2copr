%global __brp_check_rpaths %{nil}
%global packname  idmodelr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Infectious Disease Model Library and Utilities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-deSolve >= 1.23
BuildRequires:    R-CRAN-future >= 1.14.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-furrr >= 0.1.0
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-deSolve >= 1.23
Requires:         R-CRAN-future >= 1.14.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-furrr >= 0.1.0

%description
Explore a range of infectious disease models in a consistent framework.
The primary aim of 'idmodelr' is to provide a library of infectious
disease models for researchers, students, and other interested
individuals. These models can be used to understand the underlying
dynamics and as a reference point when developing models for research.
'idmodelr' also provides a range of utilities. These include: plotting
functionality; a simulation wrapper; scenario analysis tooling; an
interactive dashboard; tools for handling mult-dimensional models; and
both model and parameter look up tables. Unlike other modelling packages
such as 'pomp' (<https://kingaa.github.io/pomp/>), 'libbi'
(<http://libbi.org>) and 'EpiModel' (<http://www.epimodel.org>),
'idmodelr' serves primarily as an educational resource. It is most
comparable to epirecipes
(<http://epirecip.es/epicookbook/chapters/simple>) but provides a more
consistent framework, an R based workflow, and additional utility tooling.
After users have explored model dynamics with 'idmodelr' they may then
implement their model using one of these packages in order to utilise the
model fitting tools they provide.  For newer modellers, this package
reduces the barrier to entry by containing multiple infectious disease
models, providing a consistent framework for simulation and visualisation,
and signposting towards other, more research focussed, resources.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
