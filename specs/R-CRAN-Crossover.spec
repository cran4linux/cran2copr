%global packname  Crossover
%global packver   0.1-18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.18
Release:          1%{?dist}
Summary:          Analysis and Search of Crossover Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-crossdes >= 1.1.1
BuildRequires:    R-CRAN-CommonJavaJars >= 1.0.5
BuildRequires:    R-CRAN-rJava >= 0.8.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.3
BuildRequires:    R-CRAN-JavaGD 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-crossdes >= 1.1.1
Requires:         R-CRAN-CommonJavaJars >= 1.0.5
Requires:         R-CRAN-rJava >= 0.8.3
Requires:         R-CRAN-JavaGD 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-CRAN-xtable 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-CRAN-multcomp 
Requires:         R-stats4 
Requires:         R-CRAN-digest 

%description
Package Crossover provides different crossover designs from combinatorial
or search algorithms as well as from literature and a GUI to access them.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
