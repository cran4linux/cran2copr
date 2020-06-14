%global packname  nanop
%global packver   2.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6
Release:          2%{?dist}
Summary:          Tools for Nanoparticle Simulation and Calculation of PDF andTotal Scattering Structure Function

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-distrEx 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-distrEx 
Requires:         R-CRAN-rgl 

%description
This software package implements functions to simulate spherical,
ellipsoid and cubic polyatomic nanoparticles with arbitrary crystal
structures and to calculate the associated pair-distribution function and
X-ray/neutron total-scattering signals. It also provides a target function
that can be used for simultaneous fitting of small- and wide-angle total
scattering data in real and reciprocal spaces. The target function can be
generated either as a sum of weighted residuals for individual datasets or
as a vector of residuals suitable for optimization using multi-criteria
algorithms (e.g. Pareto methods).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
