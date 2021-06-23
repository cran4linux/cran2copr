%global __brp_check_rpaths %{nil}
%global packname  coga
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Convolution of Gamma Distributions

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
Requires:         gsl
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-cubature 

%description
Evaluation for density and distribution function of convolution of gamma
distributions in R. Two related exact methods and one approximate method
are implemented with efficient algorithm and C++ code. A quick guide for
choosing correct method and usage of this package is given in package
vignette. For the detail of methods used in this package, we refer the
user to Mathai(1982)<doi:10.1007/BF02481056>,
Moschopoulos(1984)<doi:10.1007/BF02481123>, Hu et
al.(2019)<doi:10.1007/s00180-019-00924-9>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/src_vign
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
