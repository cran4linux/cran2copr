%global packname  funtimes
%global packver   6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.1
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Time Series Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-Jmisc 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-Jmisc 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-Rdpack 

%description
Includes non-parametric estimators and tests for time series analysis. The
functions are to test for presence of possibly non-monotonic trends and
for synchronism of trends in multiple time series, using modern bootstrap
techniques and robust non-parametric difference-based estimators.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
