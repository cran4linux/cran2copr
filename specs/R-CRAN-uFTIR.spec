%global packname  uFTIR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Process and Analyze Agilent Cary 620 FTIR Microscope Images

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.4.0
Requires:         R-core >= 3.4.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 

%description
A set of tools to read, process, and summarize Agilent Cary 620 uFTIR
Microscope hyperspectral images primarily intended for microplastic
analysis.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
