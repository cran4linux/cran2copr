%global packname  LFDREmpiricalBayes
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Estimating Local False Discovery Rates Using Empirical BayesMethods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.2
Requires:         R-core >= 2.14.2
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-matrixStats 
Requires:         R-stats 
Requires:         R-CRAN-R6 

%description
New empirical Bayes methods aiming at analyzing the association of single
nucleotide polymorphisms (SNPs) to some particular disease are implemented
in this package. The package uses local false discovery rate (LFDR)
estimates of SNPs within a sample population defined as a "reference
class" and discovers if SNPs are associated with the corresponding
disease. Although SNPs are used throughout this document, other biological
data such as protein data and other gene data can be used. Karimnezhad,
Ali and Bickel, D. R. (2016) <http://hdl.handle.net/10393/34889>.

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
%{rlibdir}/%{packname}/INDEX
