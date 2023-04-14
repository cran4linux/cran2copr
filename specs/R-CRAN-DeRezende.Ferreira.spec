%global __brp_check_rpaths %{nil}
%global packname  DeRezende.Ferreira
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Zero Coupon Yield Curve Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-stats 
Requires:         R-CRAN-xts 
Requires:         R-stats 

%description
Modeling the zero coupon yield curve using the dynamic De Rezende and
Ferreira (2011) <doi:10.1002/for.1256> five factor model with variable or
fixed decaying parameters. For explanatory purposes, the package also
includes various short datasets of interest rates for the BRICS countries.

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
