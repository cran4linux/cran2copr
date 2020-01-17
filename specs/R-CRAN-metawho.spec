%global packname  metawho
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Meta-Analytical Implementation to Identify Who Benefits Mostfrom Treatments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forestmodel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forestmodel 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-stats 

%description
A tool for implementing so called 'deft' approach (see Fisher, David J.,
et al. (2017) <DOI:10.1136/bmj.j573>) and model visualization.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/develop.R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
