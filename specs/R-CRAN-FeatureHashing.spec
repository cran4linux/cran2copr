%global packname  FeatureHashing
%global packver   0.9.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1.4
Release:          3%{?dist}
Summary:          Creates a Model Matrix via Feature Hashing with a FormulaInterface

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-BH >= 1.54.0.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-digest >= 0.6.8
BuildRequires:    R-CRAN-Rcpp >= 0.11
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-digest >= 0.6.8
Requires:         R-CRAN-Rcpp >= 0.11
Requires:         R-methods 
Requires:         R-Matrix 

%description
Feature hashing, also called as the hashing trick, is a method to
transform features of a instance to a vector. Thus, it is a method to
transform a real dataset to a matrix. Without looking up the indices in an
associative array, it applies a hash function to the features and uses
their hash values as indices directly. The method of feature hashing in
this package was proposed in Weinberger et al. (2009) <arXiv:0902.2206>.
The hashing algorithm is the murmurhash3 from the 'digest' package. Please
see the README in <https://github.com/wush978/FeatureHashing> for more
information.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ftprl.R
%doc %{rlibdir}/%{packname}/runTest.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
