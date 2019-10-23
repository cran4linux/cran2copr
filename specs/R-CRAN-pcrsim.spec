%global packname  pcrsim
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Simulation of the Forensic DNA Process

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-strvalidator >= 1.6
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-gWidgets 
BuildRequires:    R-CRAN-mc2d 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-strvalidator >= 1.6
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-gWidgets 
Requires:         R-CRAN-mc2d 
Requires:         R-CRAN-plyr 

%description
Simulate the forensic DNA process: generate random or fixed DNA profiles,
create forensic samples including mixtures of diploid and haploid cells,
simulate DNA extraction, normalization, degradation, amplification
including stutters and inter-locus balance, and capillary electrophoresis.
DNA profiles are visualized as electropherograms and saved in tables. The
command pcrsim() opens up a graphical user interface which allow the user
to create projects, to enter, load, and save parameters required for the
simulation. The simulation is transparent and the parameters used in each
step of the simulation can be viewed in the result tables.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
