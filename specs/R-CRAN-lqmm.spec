%global packname  lqmm
%global packver   1.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          3%{?dist}
Summary:          Linear Quantile Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-nlme >= 3.1.124
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-SparseGrid 
Requires:         R-nlme >= 3.1.124
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-SparseGrid 

%description
Functions to fit quantile regression models for hierarchical data (2-level
nested designs) as described in Geraci and Bottai (2014, Statistics and
Computing) <doi:10.1007/s11222-013-9381-9>. A vignette is given in Geraci
(2014, Journal of Statistical Software) <doi:10.18637/jss.v057.i13> and
included in the package documents. The packages also provides functions to
fit quantile models for independent data and for count responses.

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
%{rlibdir}/%{packname}/libs
