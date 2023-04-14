%global __brp_check_rpaths %{nil}
%global packname  RCSF
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Airborne LiDAR Filtering Method Based on Cloth Simulation

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Cloth Simulation Filter (CSF) is an airborne LiDAR (Light Detection and
Ranging) ground points filtering algorithm which is based on cloth
simulation. It tries to simulate the interactions between the cloth nodes
and the corresponding LiDAR points, the locations of the cloth nodes can
be determined to generate an approximation of the ground surface
<https://www.mdpi.com/2072-4292/8/6/501/htm>.

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
