%global packname  ks
%global packver   1.11.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.5
Release:          1%{?dist}
Summary:          Kernel Smoothing

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-KernSmooth >= 2.22
BuildRequires:    R-CRAN-FNN >= 1.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.0
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-multicool 
Requires:         R-KernSmooth >= 2.22
Requires:         R-CRAN-FNN >= 1.1
Requires:         R-CRAN-mvtnorm >= 1.0.0
Requires:         R-CRAN-kernlab 
Requires:         R-Matrix 
Requires:         R-CRAN-mclust 
Requires:         R-mgcv 
Requires:         R-CRAN-multicool 

%description
Kernel smoothers for univariate and multivariate data, including
densities, density derivatives, cumulative distributions, clustering,
classification, density ridges, significant modal regions, and two-sample
hypothesis tests. Chacon & Duong (2018) <doi:10.1201/9780429485572>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
