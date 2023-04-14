%global __brp_check_rpaths %{nil}
%global packname  tseriesChaos
%global packver   0.1-13.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13.1
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Nonlinear Time Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-deSolve 

%description
Routines for the analysis of nonlinear time series. This work is largely
inspired by the TISEAN project, by Rainer Hegger, Holger Kantz and Thomas
Schreiber: <http://www.mpipks-dresden.mpg.de/~tisean/>.

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
