%global __brp_check_rpaths %{nil}
%global packname  SpatialFloor
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial Floor Simulation (Isotropic)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-taRifx 
BuildRequires:    R-CRAN-blocksdesign 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-base 
Requires:         R-CRAN-taRifx 
Requires:         R-CRAN-blocksdesign 

%description
Spatial floor simulation with exponential/Gaussian variance-covariance
function (isotropic), with specification of distance function, nugget,
sill, range. The methodology follows Nole A.C. Cressie (2015)
<doi:10.1002/9781119115151>. The original release is 2017-08-29.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
