%global packname  pdp
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          3%{?dist}
Summary:          Partial Dependence Plots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildRequires:    R-CRAN-ggplot2 >= 0.9.0
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 0.9.0
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-lattice 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-mgcv 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-viridis 
Requires:         R-utils 

%description
A general framework for constructing partial dependence (i.e., marginal
effect) plots from various types machine learning models in R.

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
