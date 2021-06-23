%global __brp_check_rpaths %{nil}
%global packname  dils
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          3%{?dist}%{?buildtag}
Summary:          Data-Informed Link Strength. Combine multiple-relationshipnetworks into a single weighted network. Impute (fill-in)missing network links.

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.10.4
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-Rcpp >= 0.10.4
Requires:         R-CRAN-igraph 

%description
Combine multiple-relationship networks into a single weighted network.
The approach is similar to factor analysis in the that contribution from
each constituent network varies so as to maximize the information gleaned
from the multiple-relationship networks. This implementation uses
Principal Component Analysis calculated using 'prcomp' with bootstrap
subsampling.  Missing links are imputed using the method of Chen et al.
(2012).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
