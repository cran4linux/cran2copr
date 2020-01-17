%global packname  ampir
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Predict Antimicrobial Peptides

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-caret >= 6.0.0
BuildRequires:    R-CRAN-Peptides 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-caret >= 6.0.0
Requires:         R-CRAN-Peptides 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-Rcpp 

%description
A toolkit to predict antimicrobial peptides from protein sequences on a
genome-wide scale. It incorporates a support vector machine model trained
on publicly available antimicrobial peptide data using calculated
physico-chemical and compositional sequence properties described in Meher
et al. (2017) <doi:10.1038/srep42362>. In order to support genome-wide
analyses this model is designed to accept any type of protein as input and
calculation of compositional properties has been optimised for
high-throughput use.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
