%global packname  nlrx
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Setup, Run and Analyze 'NetLogo' Model Simulations from 'R' via'XML'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-sensitivity 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-genalg 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-sensitivity 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-genalg 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringr 

%description
Setup, run and analyze 'NetLogo' (<https://ccl.northwestern.edu/netlogo/>)
model simulations in 'R'. 'nlrx' experiments use a similar structure as
'NetLogos' Behavior Space experiments. However, 'nlrx' offers more
flexibility and additional tools for running and analyzing complex
simulation designs and sensitivity analyses. The user defines all
information that is needed in an intuitive framework, using class objects.
Experiments are submitted from 'R' to 'NetLogo' via 'XML' files that are
dynamically written, based on specifications defined by the user. By
nesting model calls in future environments, large simulation design with
many runs can be executed in parallel. This also enables simulating
'NetLogo' experiments on remote HPC machines. In order to use this
package, 'Java' and 'NetLogo' (>= 5.3.1) need to be available on the
executing system.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
