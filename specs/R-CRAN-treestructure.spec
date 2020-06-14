%global packname  treestructure
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Detect Population Structure Within Phylogenetic Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ape >= 5.0

%description
Algorithms for detecting population structure from the history of
coalescent events recorded in phylogenetic trees. This method classifies
each tip and internal node of a tree into disjoint sets characterized by
similar coalescent patterns. The methods are described in Volz, E., Wiuf,
C., Grad, Y., Frost, S., Dennis, A., & Didelot, X. (2020)
<doi:10.1093/sysbio/syaa009>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/sim.nwk
%doc %{rlibdir}/%{packname}/treestructure.Rmd
%doc %{rlibdir}/%{packname}/tscl
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
