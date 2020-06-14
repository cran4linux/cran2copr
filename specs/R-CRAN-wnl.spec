%global packname  wnl
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          2%{?dist}
Summary:          Minimization Tool for Pharmacokinetic-Pharmacodynamic DataAnalysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-numDeriv 

%description
This is a set of minimization tools (maximum likelihood estimation and
least square fitting) to solve examples in the Johan Gabrielsson and Dan
Weiner's book "Pharmacokinetic and Pharmacodynamic Data Analysis -
Concepts and Applications" 5th ed. (ISBN:9198299107). Examples include
linear and nonlinear compartmental model, turn-over model, single or
multiple dosing bolus/infusion/oral models, allometry, toxicokinetics,
reversible metabolism, in-vitro/in-vivo extrapolation, enterohepatic
circulation, metabolite modeling, Emax model, inhibitory model, tolerance
model, oscillating response model, enantiomer interaction model, effect
compartment model, drug-drug interaction model, receptor occupancy model,
and rebound phenomena model.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
