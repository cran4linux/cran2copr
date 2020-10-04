%global packname  dodgr
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          3%{?dist}%{?buildtag}
Summary:          Distances on Directed Graphs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-osmdata 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-CRAN-callr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-osmdata 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-RcppThread 

%description
Distances on dual-weighted directed graphs using priority-queue shortest
paths (Padgham (2019) <doi:10.32866/6945>). Weighted directed graphs have
weights from A to B which may differ from those from B to A. Dual-weighted
directed graphs have two sets of such weights. A canonical example is a
street network to be used for routing in which routes are calculated by
weighting distances according to the type of way and mode of transport,
yet lengths of routes must be calculated from direct distances.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
