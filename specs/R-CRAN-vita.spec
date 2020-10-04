%global packname  vita
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Variable Importance Testing Approaches

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.6
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.11.6
Requires:         R-parallel 
Requires:         R-CRAN-randomForest 
Requires:         R-stats 

%description
Implements the novel testing approach by Janitza et al.(2015)
<http://nbn-resolving.de/urn/resolver.pl?urn=nbn:de:bvb:19-epub-25587-4>
for the permutation variable importance measure in a random forest and the
PIMP-algorithm by Altmann et al.(2010)
<doi:10.1093/bioinformatics/btq134>. Janitza et al.(2015)
<http://nbn-resolving.de/urn/resolver.pl?urn=nbn:de:bvb:19-epub-25587-4>
do not use the "standard" permutation variable importance but the
cross-validated permutation variable importance for the novel test
approach. The cross-validated permutation variable importance is not based
on the out-of-bag observations but uses a similar strategy which is
inspired by the cross-validation procedure. The novel test approach can be
applied for classification trees as well as for regression trees. However,
the use of the novel testing approach has not been tested for regression
trees so far, so this routine is meant for the expert user only and its
current state is rather experimental.

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
