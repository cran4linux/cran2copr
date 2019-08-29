%global packname  FractalParameterEstimation
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Simulation and Parameter Estimation of Randomized SierpinskiCarpets using the p-p-p-q-Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch

%description
The parameters p and q are estimated with the aid of a randomized
Sierpinski Carpet which is built on a [p-p-p-q]-model. Thereby, for three
times a simulation with a p-value and once with a q-value is assumed.
Hence, these parameters are estimated and displayed. Moreover, functions
for simulating random Sierpinski-Carpets with constant and variable
probabilities are included. For more details on the method please see
Hermann et al. (2015) <doi:10.1002/sim.6497>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
