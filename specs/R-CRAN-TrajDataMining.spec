%global __brp_check_rpaths %{nil}
%global packname  TrajDataMining
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Trajectories Data Mining

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-trajectories 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-trajectories 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-geosphere 
Requires:         R-methods 
Requires:         R-CRAN-rgdal 

%description
Contains a set of methods for trajectory data preparation, such as
filtering, compressing and clustering, and for trajectory pattern
discovery.

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
