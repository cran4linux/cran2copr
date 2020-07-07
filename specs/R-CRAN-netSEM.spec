%global packname  netSEM
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          3%{?dist}
Summary:          Network Structural Equation Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.47
BuildRequires:    R-CRAN-gtools >= 3.5.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-svglite >= 1.2.1
BuildRequires:    R-CRAN-htmlwidgets >= 1.2
BuildRequires:    R-CRAN-rsvg >= 1.1
BuildRequires:    R-CRAN-DiagrammeR >= 0.9.2
BuildRequires:    R-CRAN-segmented >= 0.5.3.0
BuildRequires:    R-CRAN-png >= 0.1.7
BuildRequires:    R-CRAN-DiagrammeRsvg >= 0.1
Requires:         R-MASS >= 7.3.47
Requires:         R-CRAN-gtools >= 3.5.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-svglite >= 1.2.1
Requires:         R-CRAN-htmlwidgets >= 1.2
Requires:         R-CRAN-rsvg >= 1.1
Requires:         R-CRAN-DiagrammeR >= 0.9.2
Requires:         R-CRAN-segmented >= 0.5.3.0
Requires:         R-CRAN-png >= 0.1.7
Requires:         R-CRAN-DiagrammeRsvg >= 0.1

%description
The network structural equation modeling conducts a network statistical
analysis on a data frame of coincident observations of multiple continuous
variables [1]. It builds a pathway model by exploring a pool of domain
knowledge guided candidate statistical relationships between each of the
variable pairs, selecting the 'best fit' on the basis of a specific
criteria such as adjusted r-squared value. This work was funded under U.
S. Dept. of Energy, Prime Award No. DE-E-0004946, Award Agreement No.
60220829-51077-T. [1] Bruckman, Laura S., Nicholas R. Wheeler, Junheng Ma,
Ethan Wang, Carl K. Wang, Ivan Chou, Jiayang Sun, and Roger H. French.
(2013) <doi:10.1109/ACCESS.2013.2267611>.

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
