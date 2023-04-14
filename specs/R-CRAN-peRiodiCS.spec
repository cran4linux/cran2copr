%global __brp_check_rpaths %{nil}
%global packname  peRiodiCS
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Generating Periodic Curves

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-rms 
Requires:         R-graphics 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-rms 

%description
Functions for generating variants of curves: restricted cubic spline,
periodic restricted cubic spline, periodic cubic spline. Periodic splines
can be used to model data that has periodic nature / seasonality.

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
