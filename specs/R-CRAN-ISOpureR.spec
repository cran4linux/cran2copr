%global packname  ISOpureR
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}
Summary:          Deconvolution of Tumour Profiles

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.2.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-futile.logger 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-stats 
Requires:         R-CRAN-futile.logger 

%description
Deconvolution of mixed tumour profiles into normal and cancer for each
patient, using the ISOpure algorithm in Quon et al. Genome Medicine, 2013
5:29. Deconvolution requires mixed tumour profiles and a set of unmatched
"basis" normal profiles.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
