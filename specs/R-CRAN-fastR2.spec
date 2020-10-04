%global packname  fastR2
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Foundations and Applications of Statistics Using R (2nd Edition)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-mosaic >= 1.3.0
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-miscTools 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-mosaic >= 1.3.0
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-dplyr 
Requires:         R-lattice 
Requires:         R-CRAN-miscTools 

%description
Data sets and utilities to accompany the second edition of "Foundations
and Applications of Statistics: an Introduction using R" (R Pruim,
published by AMS, 2017), a text covering topics from probability and
mathematical statistics at an advanced undergraduate level.  R is
integrated throughout, and access to all the R code in the book is
provided via the snippet() function.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/snippet
%{rlibdir}/%{packname}/INDEX
