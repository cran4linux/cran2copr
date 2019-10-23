%global packname  subselect
%global packver   0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14
Release:          1%{?dist}
Summary:          Selecting Variable Subsets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ISwR 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-MASS 
Requires:         R-CRAN-ISwR 
Requires:         R-CRAN-corpcor 

%description
A collection of functions which (i) assess the quality of variable subsets
as surrogates for a full data set, in either an exploratory data analysis
or in the context of a multivariate linear model, and (ii) search for
subsets which are optimal under various criteria.

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
%doc %{rlibdir}/%{packname}/CHANGELOG
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/readme
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
