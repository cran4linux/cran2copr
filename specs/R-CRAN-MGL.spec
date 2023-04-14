%global __brp_check_rpaths %{nil}
%global packname  MGL
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Module Graphical Lasso

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
An aggressive dimensionality reduction and network estimation technique
for a high-dimensional Gaussian graphical model (GGM). Please refer to:
Efficient Dimensionality Reduction for High-Dimensional Network
Estimation, Safiye Celik, Benjamin A. Logsdon, Su-In Lee, Proceedings of
The 31st International Conference on Machine Learning, 2014, p.
1953--1961.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
