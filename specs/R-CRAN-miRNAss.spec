%global packname  miRNAss
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          2%{?dist}
Summary:          Genome-Wide Discovery of Pre-miRNAs with few Labeled Examples

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-CORElearn 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-CORElearn 
Requires:         R-CRAN-RSpectra 

%description
Machine learning method specifically designed for pre-miRNA prediction. It
takes advantage of unlabeled sequences to improve the prediction rates
even when there are just a few positive examples, when the negative
examples are unreliable or are not good representatives of its class.
Furthermore, the method can automatically search for negative examples if
the user is unable to provide them. MiRNAss can find a good boundary to
divide the pre-miRNAs from other groups of sequences; it automatically
optimizes the threshold that defines the classes boundaries, and thus, it
is robust to high class imbalance. Each step of the method is scalable and
can handle large volumes of data.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
