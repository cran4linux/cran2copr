%global packname  opusminer
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          OPUS Miner Algorithm for Filtered Top-k Association Discovery

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-arules >= 1.5.0
BuildRequires:    R-Matrix >= 1.2.7
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-methods 
Requires:         R-CRAN-arules >= 1.5.0
Requires:         R-Matrix >= 1.2.7
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-methods 

%description
Provides a simple R interface to the OPUS Miner algorithm (implemented in
C++) for finding the top-k productive, non-redundant itemsets from
transaction data.  The OPUS Miner algorithm uses the OPUS search algorithm
to efficiently discover the key associations in transaction data, in the
form of self-sufficient itemsets, using either leverage or lift.  See
<http://i.giwebb.com/index.php/research/association-discovery/> for more
information in relation to the OPUS Miner algorithm.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
