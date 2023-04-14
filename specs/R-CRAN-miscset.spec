%global __brp_check_rpaths %{nil}
%global packname  miscset
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Miscellaneous Tools Set

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-xtable 

%description
A collection of miscellaneous methods to simplify various tasks, including
plotting, data.frame and matrix transformations, environment functions,
regular expression methods, and string and logical operations, as well as
numerical and statistical tools. Most of the methods are simple but useful
wrappers of common base R functions, which extend S3 generics or provide
default values for important parameters.

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
