%global __brp_check_rpaths %{nil}
%global packname  tdr
%global packver   0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13
Release:          3%{?dist}%{?buildtag}
Summary:          Target Diagram

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-lattice 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Implementation of target diagrams using 'lattice' and 'ggplot2' graphics.
Target diagrams provide a graphical overview of the respective
contributions of the unbiased RMSE and MBE to the total RMSE (Jolliff, J.
et al., 2009. "Summary Diagrams for Coupled Hydrodynamic-Ecosystem Model
Skill Assessment." Journal of Marine Systems 76: 64–82.)

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
