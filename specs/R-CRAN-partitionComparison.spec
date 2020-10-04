%global packname  partitionComparison
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          3%{?dist}%{?buildtag}
Summary:          Implements Measures for the Comparison of Two Partitions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-methods 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-lpSolve 

%description
Provides several measures ((dis)similarity, distance/metric, correlation,
entropy) for comparing two partitions of the same set of objects. The
different measures can be assigned to three different classes: Pair
comparison (containing the famous Jaccard and Rand indices), set based,
and information theory based. Many of the implemented measures can be
found in Albatineh AN, Niewiadomska-Bugaj M and Mihalko D (2006)
<doi:10.1007/s00357-006-0017-z> and Meila M (2007)
<doi:10.1016/j.jmva.2006.11.013>. Partitions are represented by vectors of
class labels which allow a straightforward integration with existing
clustering algorithms (e.g. kmeans()). The package is mostly based on the
S4 object system.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
