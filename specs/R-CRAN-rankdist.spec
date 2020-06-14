%global packname  rankdist
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          2%{?dist}
Summary:          Distance Based Ranking Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-CRAN-hash 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-permute 
Requires:         R-methods 

%description
Implements distance based probability models for ranking data. The
supported distance metrics include Kendall distance, Spearman distance,
Footrule distance, Hamming distance, Weighted-tau distance and Weighted
Kendall distance. Phi-component model and mixture models are also
supported.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
