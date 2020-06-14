%global packname  HistogramTools
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}
Summary:          Utility Functions for R Histograms

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-ash 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-ash 
Requires:         R-CRAN-stringr 

%description
Provides a number of utility functions useful for manipulating large
histograms.  This includes methods to trim, subset, merge buckets, merge
histograms, convert to CDF, and calculate information loss due to binning.
It also provides a protocol buffer representations of the default R
histogram class to allow histograms over large data sets to be computed
and manipulated in a MapReduce environment.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/proto
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
