%global packname  KernSmoothIRT
%global packver   6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.4
Release:          3%{?dist}
Summary:          Nonparametric Item Response Theory

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-rgl 
Requires:         R-methods 

%description
Fits nonparametric item and option characteristic curves using kernel
smoothing. It allows for optimal selection of the smoothing bandwidth
using cross-validation and a variety of exploratory plotting tools. The
kernel smoothing is based on methods described in Silverman, B.W. (1986).
Density Estimation for Statistics and Data Analysis. Chapman & Hall,
London.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
