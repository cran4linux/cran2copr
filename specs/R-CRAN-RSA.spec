%global packname  RSA
%global packver   0.9.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.13
Release:          1%{?dist}
Summary:          Response Surface Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.5.20
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-aplpack 
BuildRequires:    R-CRAN-tkrplot 
Requires:         R-CRAN-lavaan >= 0.5.20
Requires:         R-CRAN-ggplot2 
Requires:         R-lattice 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-aplpack 
Requires:         R-CRAN-tkrplot 

%description
Advanced response surface analysis. The main function RSA computes and
compares several nested polynomial regression models (full polynomial,
shifted and rotated squared differences, rising ridge surfaces, basic
squared differences). The package provides plotting functions for 3d
wireframe surfaces, interactive 3d plots, and contour plots. Calculates
many surface parameters (a1 to a4, principal axes, stationary point,
eigenvalues) and provides standard, robust, or bootstrapped standard
errors and confidence intervals for them.

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
%doc %{rlibdir}/%{packname}/News.Rd
%doc %{rlibdir}/%{packname}/RSA_modeltree.pdf
%{rlibdir}/%{packname}/INDEX
