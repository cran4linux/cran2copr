%global packname  linpk
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Generate Concentration-Time Profiles from Linear PK Systems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-mvtnorm 

%description
Generate concentration-time profiles from linear pharmacokinetic (PK)
systems, possibly with first-order absorption or zero-order infusion,
possibly with one or more peripheral compartments, and possibly under
steady-state conditions. Single or multiple doses may be specified.
Secondary (derived) PK parameters (e.g. Cmax, Ctrough, AUC, Tmax,
half-life, etc.) are computed.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/demo-app
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
