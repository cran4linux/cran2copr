%global packname  nlsr
%global packver   2019.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.9.7
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Nonlinear Least Squares Solutions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-digest 

%description
Provides tools for working with nonlinear least squares problems. It is
intended to eventually supersede the 'nls()' function in the R
distribution. For example, 'nls()' specifically does NOT deal with small
or zero residual problems as its Gauss-Newton method frequently stops with
'singular gradient' messages. 'nlsr' is based on the now-deprecated
package 'nlmrt', and has refactored functions and R-language symbolic
derivative features.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
