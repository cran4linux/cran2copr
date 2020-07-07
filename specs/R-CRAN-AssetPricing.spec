%global packname  AssetPricing
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Optimal Pricing of Assets with Fixed Expiry Date

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 0.99
Requires:         R-core >= 0.99
BuildArch:        noarch
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-deSolve 

%description
Calculates the optimal price of assets (such as airline flight seats,
hotel room bookings) whose value becomes zero after a fixed ``expiry
date''.  Assumes potential customers arrive (possibly in groups) according
to a known inhomogeneous Poisson process.  Also assumes a known
time-varying elasticity of demand (price sensitivity) function.  Uses
elementary techniques based on ordinary differential equations.  Uses the
package deSolve to effect the solution of these differential equations.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/coa
%doc %{rlibdir}/%{packname}/optimNote.tex
%doc %{rlibdir}/%{packname}/plot.flap.R.old
%{rlibdir}/%{packname}/INDEX
