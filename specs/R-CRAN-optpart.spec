%global packname  optpart
%global packver   3.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          3%{?dist}
Summary:          Optimal Partitioning of Similarity Relations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-labdsv 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-cluster 
Requires:         R-CRAN-labdsv 
Requires:         R-MASS 
Requires:         R-CRAN-plotrix 

%description
Contains a set of algorithms for creating partitions and coverings of
objects largely based on operations on (dis)similarity relations (or
matrices). There are several iterative re-assignment algorithms optimizing
different goodness-of-clustering criteria.  In addition, there are
covering algorithms 'clique' which derives maximal cliques, and 'maxpact'
which creates a covering of maximally compact sets. Graphical analyses and
conversion routines are also included.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
