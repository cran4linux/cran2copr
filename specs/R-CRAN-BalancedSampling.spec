%global __brp_check_rpaths %{nil}
%global packname  BalancedSampling
%global packver   1.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          3%{?dist}%{?buildtag}
Summary:          Balanced and Spatially Balanced Sampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-SamplingBigData 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-SamplingBigData 

%description
Select balanced and spatially balanced probability samples in
multi-dimensional spaces with any prescribed inclusion probabilities. It
contains fast (C++ via Rcpp) implementations of the included sampling
methods. The local pivotal method and spatially correlated Poisson
sampling (for spatially balanced sampling) are included. Also the cube
method (for balanced sampling) and the local cube method (for doubly
balanced sampling) are included.

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
