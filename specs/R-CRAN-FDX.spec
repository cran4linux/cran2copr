%global packname  FDX
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          False Discovery Exceedance Controlling Multiple TestingProcedures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-DiscreteFDR 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-PoissonBinomial 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-DiscreteFDR 
Requires:         R-methods 
Requires:         R-CRAN-PoissonBinomial 
Requires:         R-CRAN-pracma 

%description
Multiple testing procedures for heterogeneous and discrete tests as
described in Döhler and Roquain (2019) <arXiv:1912.04607v1>. The main
algorithms of the paper are available as continuous, discrete and weighted
versions.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
