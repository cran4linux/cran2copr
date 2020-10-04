%global packname  hdrcde
%global packver   3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Highest Density Regions and Conditional Density Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-CRAN-ash 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-locfit 
Requires:         R-CRAN-ash 
Requires:         R-CRAN-ks 
Requires:         R-KernSmooth 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RColorBrewer 

%description
Computation of highest density regions in one and two dimensions, kernel
estimation of univariate density functions conditional on one
covariate,and multimodal regression.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
