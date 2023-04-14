%global __brp_check_rpaths %{nil}
%global packname  smatr
%global packver   3.4-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.8
Release:          3%{?dist}%{?buildtag}
Summary:          (Standardised) Major Axis Estimation and Testing Routines

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Methods for fitting bivariate lines in allometry using the major axis (MA)
or standardised major axis (SMA), and for making inferences about such
lines. The available methods of inference include confidence intervals and
one-sample tests for slope and elevation, testing for a common slope or
elevation amongst several allometric lines, constructing a confidence
interval for a common slope or elevation, and testing for no shift along a
common axis, amongst several samples. See Warton et al. 2012
<doi:10.1111/j.2041-210X.2011.00153.x> for methods description.

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
