%global packname  psgp
%global packver   0.3-19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.19
Release:          3%{?dist}%{?buildtag}
Summary:          Projected Spatial Gaussian Process Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.0
BuildRequires:    R-CRAN-intamap 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-intamap 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-automap 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 

%description
Implements projected sparse Gaussian process Kriging (Ingram 'et. al.',
2008, <doi:10.1007/s00477-007-0163-9>) as an additional method for the
'intamap' package. More details on implementation (Barillec 'et. al.',
2010, <doi:10.1016/j.cageo.2010.05.008>).

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
