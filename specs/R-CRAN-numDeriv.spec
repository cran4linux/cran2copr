%global __brp_check_rpaths %{nil}
%global packname  numDeriv
%global packver   2016.8-1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2016.8.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Accurate Numerical Derivatives

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.11.1
Requires:         R-core >= 2.11.1
BuildArch:        noarch

%description
Methods for calculating (usually) accurate numerical first and second
order derivatives. Accurate calculations are done using 'Richardson''s'
extrapolation or, when applicable, a complex step derivative is available.
A simple difference method is also provided. Simple difference is
(usually) less accurate but is much quicker than 'Richardson''s'
extrapolation and provides a useful cross-check. Methods are provided for
real scalar and vector valued functions.

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
