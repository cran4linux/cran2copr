%global __brp_check_rpaths %{nil}
%global packname  InvasionCorrection
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Invasion Correction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-utils 

%description
The correction is achieved under the assumption that non-migrating cells
of the essay approximately form a quadratic flow profile due to frictional
effects, compare law of Hagen-Poiseuille for flow in a tube. The script
fits a conical plane to give xyz-coordinates of the cells. It outputs the
number of migrated cells and the new corrected coordinates.

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
