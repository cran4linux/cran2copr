%global packname  fractalrock
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Generate fractal time series with non-normal returnsdistribution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-futile.any >= 1.3.0
BuildRequires:    R-CRAN-futile.logger >= 1.3.0
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-quantmod 
Requires:         R-CRAN-futile.any >= 1.3.0
Requires:         R-CRAN-futile.logger >= 1.3.0
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-quantmod 

%description
The basic principle driving fractal generation of time series is that data
is generated iteratively based on increasing levels of resolution.  The
initial series is defined by a so-called initiator pattern and then
generators are used to replace each segment of the initial pattern.
Regular, repeatable patterns can be produced by using the same seed and
generators.  By using a set of generators, non-repeatable time series can
be produced.  This technique is the basis of the fractal time series
process in this package.

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
