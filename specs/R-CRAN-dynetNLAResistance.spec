%global __brp_check_rpaths %{nil}
%global packname  dynetNLAResistance
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Resisting Neighbor Label Attack in a Dynamic Network

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-parallel 

%description
An anonymization algorithm to resist neighbor label attack in a dynamic
network.

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
