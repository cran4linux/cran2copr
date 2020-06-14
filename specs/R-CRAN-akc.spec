%global packname  akc
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          2%{?dist}
Summary:          Automatic Knowledge Classification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.6
BuildRequires:    R-CRAN-tidygraph >= 1.1.2
BuildRequires:    R-CRAN-ggraph >= 1.0.2
BuildRequires:    R-CRAN-ggwordcloud >= 0.5.0
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-textstem 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-widyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-data.table >= 1.12.6
Requires:         R-CRAN-tidygraph >= 1.1.2
Requires:         R-CRAN-ggraph >= 1.0.2
Requires:         R-CRAN-ggwordcloud >= 0.5.0
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-textstem 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-widyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 

%description
A tidy framework for automatic knowledge classification and visualization.
Currently, the core functionality of the framework is mainly supported by
modularity-based clustering (community detection) in keyword co-occurrence
network, and focuses on co-word analysis of bibliometric research.
However, the designed functions in 'akc' are general, and could be
extended to solve other tasks in text mining as well.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
