%global packname  walrus
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Robust Statistical Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jmvcore >= 0.9.1
BuildRequires:    R-CRAN-WRS2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-jmvcore >= 0.9.1
Requires:         R-CRAN-WRS2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-R6 

%description
A toolbox of common robust statistical tests, including robust
descriptives, robust t-tests, and robust ANOVA. It is also available as a
module for 'jamovi' (see <https://www.jamovi.org> for more information).
Walrus is based on the WRS2 package by Patrick Mair, which is in turn
based on the scripts and work of Rand Wilcox. These analyses are described
in depth in the book 'Introduction to Robust Estimation & Hypothesis
Testing'.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
