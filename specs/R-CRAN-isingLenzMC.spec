%global __brp_check_rpaths %{nil}
%global packname  isingLenzMC
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          3%{?dist}%{?buildtag}
Summary:          Monte Carlo for Classical Ising Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0

%description
Classical Ising Model is a land mark system in statistical physics.The
model explains the physics of spin glasses and magnetic materials, and
cooperative phenomenon in general, for example phase transitions and
neural networks.This package provides utilities to simulate one
dimensional Ising Model with Metropolis and Glauber Monte Carlo with
single flip dynamics in periodic boundary conditions. Utility functions
for exact solutions are provided.

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
