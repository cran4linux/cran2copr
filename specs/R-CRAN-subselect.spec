%global packname  subselect
%global packver   0.15.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15.2
Release:          2%{?dist}
Summary:          Selecting Variable Subsets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
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
subsets which are optimal under various criteria. Theoretical support for
the heuristic search methods and exploratory data analysis criteria is in
Cadima, Cerdeira, Minhoto (2003, <doi:10.1016/j.csda.2003.11.001>).
Theoretical support for the leap and bounds algorithm and the criteria for
the general multivariate linear model is in Duarte Silva (2001,
<doi:10.1006/jmva.2000.1920>). There is a package vignette "subselect",
which includes additional references.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CHANGELOG
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/readme
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
