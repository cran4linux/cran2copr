%global packname  fastcluster
%global packver   1.1.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.25
Release:          2%{?dist}
Summary:          Fast Hierarchical Clustering Routines for R and 'Python'

License:          FreeBSD | GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
This is a two-in-one package which provides interfaces to both R and
'Python'. It implements fast hierarchical, agglomerative clustering
routines. Part of the functionality is designed as drop-in replacement for
existing routines: linkage() in the 'SciPy' package
'scipy.cluster.hierarchy', hclust() in R's 'stats' package, and the
'flashClust' package. It provides the same functionality with the benefit
of a much faster implementation. Moreover, there are memory-saving
routines for clustering of vector data, which go beyond what the existing
packages provide. For information on how to install the 'Python' files,
see the file INSTALL in the source distribution. Based on the present
package, Christoph Dalitz also wrote a pure 'C++' interface to
'fastcluster': <http://informatik.hsnr.de/~dalitz/data/hclust>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
