%global __brp_check_rpaths %{nil}
%global packname  ODEsensitivity
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis of Ordinary Differential Equations

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ODEnetwork >= 1.3.0
BuildRequires:    R-CRAN-sensitivity >= 1.12.1
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-ODEnetwork >= 1.3.0
Requires:         R-CRAN-sensitivity >= 1.12.1
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-deSolve 

%description
Performs sensitivity analysis in ordinary differential equation (ode)
models. The package utilize the ode interface from 'deSolve' and connects
it with the sensitivity analysis from 'sensitivity'. Additionally we add a
method to run the sensitivity analysis on variables with class
'ODEnetwork'. A detailed plotting function provides outputs on the
calculations. The method is described by Weber, Theers, Surmann, Ligges,
and Weihs (2018) <doi:10.17877/DE290R-18874>.

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
