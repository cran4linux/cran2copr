%global packname  SMITIDvisu
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          2%{?dist}
Summary:          Visualize Data for Host and Viral Population from 'SMITIDstruct'using HTMLwidgets

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-yaml >= 2.1.16
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-htmlwidgets >= 0.3.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-yaml >= 2.1.16
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-htmlwidgets >= 0.3.2
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-utils 
Requires:         R-CRAN-magrittr 

%description
Visualisation tools for 'SMITIDstruct' package. Allow to visualize host
timeline, transmission tree, index diversities and variant graph using
HTMLwidgets. It mainly using D3JS javascript framework.

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
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
