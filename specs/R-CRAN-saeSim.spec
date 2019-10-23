%global packname  saeSim
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}
Summary:          Simulation Tools for Small Area Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-functional 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-parallelMap 
Requires:         R-CRAN-dplyr >= 0.2
Requires:         R-methods 
Requires:         R-CRAN-functional 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-utils 
Requires:         R-CRAN-spdep 
Requires:         R-stats 
Requires:         R-CRAN-parallelMap 

%description
Tools for the simulation of data in the context of small area estimation.
Combine all steps of your simulation - from data generation over drawing
samples to model fitting - in one object. This enables easy modification
and combination of different scenarios. You can store your results in a
folder or start the simulation in parallel.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
