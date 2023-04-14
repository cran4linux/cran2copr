%global __brp_check_rpaths %{nil}
%global packname  dispmod
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Modelling Dispersion in GLM

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Functions for estimating Gaussian dispersion regression models (Aitkin,
1987 <doi:10.2307/2347792>), overdispersed binomial logit models
(Williams, 1987 <doi:10.2307/2347977>), and overdispersed Poisson
log-linear models (Breslow, 1984 <doi:10.2307/2347661>), using a
quasi-likelihood approach.

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
