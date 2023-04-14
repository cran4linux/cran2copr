%global __brp_check_rpaths %{nil}
%global packname  calibrar
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Automated Parameter Estimation for Complex (Ecological) Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-cmaes 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cmaes 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Automated parameter estimation for complex (ecological) models in R. This
package allows the parameter estimation or calibration of complex models,
including stochastic ones. It is a generic tool that can be used for
fitting any type of models, especially those with non-differentiable
objective functions. It supports multiple phases and constrained
optimization. It implements maximum likelihood estimation methods and
automated construction of the objective function from simulated model
outputs. See <http://roliveros-ramos.github.io/calibrar> for more details.

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
