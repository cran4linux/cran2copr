%global __brp_check_rpaths %{nil}
%global packname  benchr
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          3%{?dist}%{?buildtag}
Summary:          High Precise Measurement of R Expressions Execution Time

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-RcppProgress 
Requires:         R-stats 
Requires:         R-graphics 

%description
Provides infrastructure to accurately measure and compare the execution
time of R expressions.

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
%{rlibdir}/%{packname}
