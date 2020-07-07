%global packname  delayed
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          A Framework for Parallelizing Dependent Tasks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-rstackdeque 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-future 
Requires:         R-CRAN-rstackdeque 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-progress 

%description
Mechanisms to parallelize dependent tasks in a manner that optimizes the
compute resources available. It provides access to "delayed" computations,
which may be parallelized using futures. It is, to an extent, a facsimile
of the 'Dask' library (<https://dask.org/>), for the 'Python' language.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
