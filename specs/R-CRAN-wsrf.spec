%global packname  wsrf
%global packver   1.7.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.17
Release:          3%{?dist}
Summary:          Weighted Subspace Random Forest for Classification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.2
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.10.2
Requires:         R-parallel 
Requires:         R-stats 

%description
A parallel implementation of Weighted Subspace Random Forest.  The
Weighted Subspace Random Forest algorithm was proposed in the
International Journal of Data Warehousing and Mining by Baoxun Xu, Joshua
Zhexue Huang, Graham Williams, Qiang Wang, and Yunming Ye (2012)
<DOI:10.4018/jdwm.2012040103>.  The algorithm can classify very
high-dimensional data with random forests built using small subspaces.  A
novel variable weighting method is used for variable subspace selection in
place of the traditional random variable sampling.This new approach is
particularly useful in building models from high-dimensional data.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
