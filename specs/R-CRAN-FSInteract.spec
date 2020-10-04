%global packname  FSInteract
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Fast Searches for Interactions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Performs fast detection of interactions in large-scale data using the
method of random intersection trees introduced in Shah, R. D. and
Meinshausen, N. (2014) <http://www.jmlr.org/papers/v15/shah14a.html>. The
algorithm finds potentially high-order interactions in high-dimensional
binary two-class classification data, without requiring lower order
interactions to be informative.  The search is particularly fast when the
matrices of predictors are sparse.  It can also be used to perform market
basket analysis when supplied with a single binary data matrix.  Here it
will find collections of columns which for many rows contain all 1's.

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
