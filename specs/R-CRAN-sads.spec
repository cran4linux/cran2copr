%global __brp_check_rpaths %{nil}
%global packname  sads
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Models for Species Abundance Distributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-bbmle >= 1.0.19
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-poilog 
BuildRequires:    R-CRAN-GUILDS 
Requires:         R-CRAN-bbmle >= 1.0.19
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-poilog 
Requires:         R-CRAN-GUILDS 

%description
Maximum likelihood tools to fit and compare models of species abundance
distributions and of species rank-abundance distributions.

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
