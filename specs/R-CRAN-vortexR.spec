%global packname  vortexR
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          3%{?dist}
Summary:          Post Vortex Simulation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.4.2
BuildRequires:    R-CRAN-GGally >= 1.5.0
BuildRequires:    R-CRAN-vortexRdata >= 1.0.3
BuildRequires:    R-CRAN-irr >= 0.84.1
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmulti 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-gtools >= 3.4.2
Requires:         R-CRAN-GGally >= 1.5.0
Requires:         R-CRAN-vortexRdata >= 1.0.3
Requires:         R-CRAN-irr >= 0.84.1
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmulti 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-stringr 

%description
Facilitate Post Vortex Simulation Analysis by offering tools to collate
multiple Vortex (v10) output files into one R object, and analyse the
collated output statistically. Vortex is a software for the development of
individual-based model for population dynamic simulation (see
<https://scti.tools/vortex/>).

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
%{rlibdir}/%{packname}/INDEX
