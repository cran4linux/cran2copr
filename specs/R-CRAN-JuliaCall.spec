%global packname  JuliaCall
%global packver   0.17.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.1
Release:          3%{?dist}%{?buildtag}
Summary:          Seamless Integration Between R and 'Julia'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         julia
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-knitr >= 1.18
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-utils 
Requires:         R-CRAN-knitr >= 1.18
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-utils 

%description
Provides an R interface to 'Julia', which is a high-level,
high-performance dynamic programming language for numerical computing, see
<https://julialang.org/> for more information. It provides a high-level
interface as well as a low-level interface. Using the high level
interface, you could call any 'Julia' function just like any R function
with automatic type conversion. Using the low level interface, you could
deal with C-level SEXP directly while enjoying the convenience of using a
high-level programming language like 'Julia'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/julia
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
