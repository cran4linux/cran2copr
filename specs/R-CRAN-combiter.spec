%global __brp_check_rpaths %{nil}
%global packname  combiter
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Combinatorics Iterators

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-itertools 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-itertools 
Requires:         R-CRAN-Rcpp 

%description
Provides iterators for combinations, permutations, subsets, and Cartesian
product, which allow one to go through all elements without creating a
huge set of all possible values.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
