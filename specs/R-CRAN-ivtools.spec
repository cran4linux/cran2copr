%global packname  ivtools
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          3%{?dist}
Summary:          Instrumental Variables

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-ahaz 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-nleqslv 
Requires:         R-survival 
Requires:         R-CRAN-ahaz 
Requires:         R-CRAN-Rcpp 

%description
Contains tools for instrumental variables estimation. Currently,
non-parametric bounds, two-stage estimation and G-estimation are
implemented. Balke, A. and Pearl, J. (1997) <doi:10.2307/2965583>,
Vansteelandt S., Bowden J., Babanezhad M., Goetghebeur E. (2011)
<doi:10.1214/11-STS360>.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
