%global packname  drake
%global packver   7.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.7.0
Release:          1%{?dist}
Summary:          A Pipeline Toolkit for Reproducible Computation at Scale

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-storr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-txtq >= 0.1.3
BuildRequires:    R-CRAN-base64url 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-storr >= 1.1.0
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-txtq >= 0.1.3
Requires:         R-CRAN-base64url 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-utils 

%description
A general-purpose computational engine for data analysis, drake rebuilds
intermediate data objects when their dependencies change, and it skips
work when the results are already up to date.  Not every execution starts
from scratch, there is native support for parallel and distributed
computing, and completed projects have tangible evidence that they are
reproducible.  Extensive documentation, from beginner-friendly tutorials
to practical examples and more, is available at the reference website
<https://docs.ropensci.org/drake/> and the online manual
<https://ropenscilabs.github.io/drake-manual/>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/templates
%doc %{rlibdir}/%{packname}/testing
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
