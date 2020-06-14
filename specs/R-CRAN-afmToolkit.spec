%global packname  afmToolkit
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Functions for Atomic Force Microscope Force-Distance CurvesAnalysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-minpack.lm 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-tibble 

%description
Set of functions for analyzing Atomic Force Microscope (AFM)
force-distance curves. It allows to obtain the contact and unbinding
points, perform the baseline correction, estimate the Young's modulus, fit
up to two exponential decay function to a stress-relaxation / creep
experiment, obtain adhesion energies. These operations can be done either
over a single F-d curve or over a set of F-d curves in batch mode.

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
%doc %{rlibdir}/%{packname}/afmexperiment
%doc %{rlibdir}/%{packname}/force-save-JPK-2h.txt.gz
%doc %{rlibdir}/%{packname}/force-save-JPK-3h.txt.gz
%doc %{rlibdir}/%{packname}/veeco_file.txt.gz
%doc %{rlibdir}/%{packname}/veecoFolder
%{rlibdir}/%{packname}/INDEX
