%global __brp_check_rpaths %{nil}
%global packname  hydroTSM
%global packver   0.6-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          3%{?dist}%{?buildtag}
Summary:          Time Series Management, Analysis and Interpolation forHydrological Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.2
BuildRequires:    R-CRAN-sp >= 1.1.0
BuildRequires:    R-CRAN-xts >= 0.9.7
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-zoo >= 1.7.2
Requires:         R-CRAN-sp >= 1.1.0
Requires:         R-CRAN-xts >= 0.9.7
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-automap 
Requires:         R-lattice 
Requires:         R-CRAN-maptools 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
S3 functions for management, analysis, interpolation and plotting of time
series used in hydrology and related environmental sciences. In
particular, this package is highly oriented to hydrological modelling
tasks. The focus of this package has been put in providing a collection of
tools useful for the daily work of hydrologists (although an effort was
made to optimise each function as much as possible, functionality has had
priority over speed). Bugs / comments / questions / collaboration of any
kind are very welcomed, and in particular, datasets that can be included
in this package for academic purposes.

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
%{rlibdir}/%{packname}
