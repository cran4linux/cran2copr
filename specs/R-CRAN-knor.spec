%global packname  knor
%global packver   0.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Non-Uniform Memory Access ('NUMA') Optimized, Parallel K-Means

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
Requires:         R-CRAN-Rcpp >= 0.12.8

%description
The k-means 'NUMA' Optimized Routine library or 'knor' is a highly
optimized and fast library for computing k-means in parallel with
accelerations for Non-Uniform Memory Access ('NUMA') architectures. Disa
Mhembere, Da Zheng, Carey E. Priebe, Joshua T. Vogelstein, Randal Burns
(2017) <arXiv:1606.08905>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
