%global __brp_check_rpaths %{nil}
%global packname  mixedsde
%global packver   5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation Methods for Stochastic Differential Mixed EffectsModels

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-sde 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-sde 
Requires:         R-CRAN-moments 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-plot3D 
Requires:         R-grDevices 

%description
Inference on stochastic differential models Ornstein-Uhlenbeck or
Cox-Ingersoll-Ross, with one or two random effects in the drift function.

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
