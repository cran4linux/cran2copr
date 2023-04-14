%global __brp_check_rpaths %{nil}
%global packname  astrodatR
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Astronomical Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A collection of 19 datasets from contemporary astronomical research.  They
are described the textbook `Modern Statistical Methods for Astronomy with
R Applications' by Eric D. Feigelson and G. Jogesh Babu (Cambridge
University Press, 2012, Appendix C) or on the website of Penn State's
Center for Astrostatistics (http://astrostatistics.psu.edu/datasets).
These datasets can be used to exercise methodology involving: density
estimation; heteroscedastic measurement errors; contingency tables;
two-sample hypothesis tests; spatial point processes; nonlinear
regression; mixture models; censoring and truncation; multivariate
analysis; classification and clustering; inhomogeneous Poisson processes;
periodic and stochastic time series analysis.

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
