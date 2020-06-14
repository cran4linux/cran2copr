%global packname  refinr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Cluster and Merge Similar Values Within a Character Vector

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-stringdist >= 0.9.5.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-stringdist >= 0.9.5.1
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-stringi 

%description
These functions take a character vector as input, identify and cluster
similar values, and then merge clusters together so their values become
identical. The functions are an implementation of the key collision and
ngram fingerprint algorithms from the open source tool Open Refine
<http://openrefine.org/>. More info on key collision and ngram fingerprint
can be found here
<https://github.com/OpenRefine/OpenRefine/wiki/Clustering-In-Depth>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
