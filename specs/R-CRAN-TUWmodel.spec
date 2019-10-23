%global packname  TUWmodel
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Lumped/Semi-Distributed Hydrological Model for EducationPurposes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-stats 
Requires:         R-stats 

%description
The model, developed at the Vienna University of Technology, is a lumped
conceptual rainfall-runoff model, following the structure of the HBV
model. The model can also be run in a semi-distributed fashion. The model
runs on a daily or shorter time step and consists of a snow routine, a
soil moisture routine and a flow routing routine. See Parajka, J., R.
Merz, G. Bloeschl (2007) <DOI:10.1002/hyp.6253> Uncertainty and multiple
objective calibration in regional water balance modelling: case study in
320 Austrian catchments, Hydrological Processes, 21, 435-446.

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
%{rlibdir}/%{packname}/libs
