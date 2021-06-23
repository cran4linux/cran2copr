%global __brp_check_rpaths %{nil}
%global packname  acss
%global packver   0.2-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          3%{?dist}%{?buildtag}
Summary:          Algorithmic Complexity for Short Strings

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-acss.data 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-acss.data 
Requires:         R-CRAN-zoo 

%description
Main functionality is to provide the algorithmic complexity for short
strings, an approximation of the Kolmogorov Complexity of a short string
using the coding theorem method (see ?acss). The database containing the
complexity is provided in the data only package acss.data, this package
provides functions accessing the data such as prob_random returning the
posterior probability that a given string was produced by a random
process. In addition, two traditional (but problematic) measures of
complexity are also provided: entropy and change complexity.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
