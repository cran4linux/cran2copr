%global packname  divDyn
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          3%{?dist}
Summary:          Diversity Dynamics using Fossil Sampling Data

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Functions to describe sampling and diversity dynamics of fossil occurrence
datasets (e.g. from the Paleobiology Database). The package includes
methods to calculate range- and occurrence-based metrics of taxonomic
richness, extinction and origination rates, along with traditional
sampling measures. A powerful subsampling tool is also included that
implements frequently used sampling standardization methods in a multiple
bin-framework. The plotting of time series and the occurrence data can be
simplified by the functions incorporated in the package, as well other
calculations, such as environmental affinities and extinction selectivity
testing. Details can be found in: Kocsis, A.T.; Reddin, C.J.; Alroy, J.
and Kiessling, W. (2019) <doi:10.1101/423780>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
