%global __brp_check_rpaths %{nil}
%global packname  fdatest
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Interval Testing Procedure for Functional Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
Requires:         R-CRAN-fda 

%description
Implementation of the Interval Testing Procedure for functional data in
different frameworks (i.e., one or two-population frameworks, functional
linear models) by means of different basis expansions (i.e., B-spline,
Fourier, and phase-amplitude Fourier). The current version of the package
requires functional data evaluated on a uniform grid; it automatically
projects each function on a chosen functional basis; it performs the
entire family of multivariate tests; and, finally, it provides the matrix
of the p-values of the previous tests and the vector of the corrected
p-values. The functional basis, the coupled or uncoupled scenario, and the
kind of test can be chosen by the user. The package provides also a
plotting function creating a graphical output of the procedure: the
p-value heat-map, the plot of the corrected p-values, and the plot of the
functional data.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
