%global __brp_check_rpaths %{nil}
%global packname  nlmrt
%global packver   2016.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2016.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Nonlinear Least Squares Solutions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch

%description
Replacement for nls() tools for working with nonlinear least squares
problems. The calling structure is similar to, but much simpler than, that
of the nls() function. Moreover, where nls() specifically does NOT deal
with small or zero residual problems, nlmrt is quite happy to solve them.
It also attempts to be more robust in finding solutions, thereby avoiding
'singular gradient' messages that arise in the Gauss-Newton method within
nls(). The Marquardt-Nash approach in nlmrt generally works more reliably
to get a solution, though this may be one of a set of possibilities, and
may also be statistically unsatisfactory. Added print and summary as of
August 28, 2012.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/dev-codes
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
