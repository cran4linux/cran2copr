%global packname  TestCor
%global packver   0.0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.0
Release:          1%{?dist}
Summary:          FWER and FDR Controlling Procedures for Multiple CorrelationTests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-MASS 
Requires:         R-stats 

%description
Different multiple testing procedures for correlation tests are
implemented. These procedures were shown to theoretically control
asymptotically the Family Wise Error Rate (Roux (2018)
<https://tel.archives-ouvertes.fr/tel-01971574v1>) or the False Discovery
Rate (Cai & Liu (2016) <doi:10.1080/01621459.2014.999157>). The package
gather four test statistics used in correlation testing, four FWER
procedures with either single step or stepdown versions, and four FDR
procedures.

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
%{rlibdir}/%{packname}/libs
