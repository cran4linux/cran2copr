%global packname  gptk
%global packver   1.08
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.08
Release:          3%{?dist}
Summary:          Gaussian Processes Tool-Kit

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-fields 
Requires:         R-Matrix 
Requires:         R-CRAN-fields 

%description
The gptk package implements a general-purpose toolkit for Gaussian process
regression with a variety of covariance functions (e.g. RBF, Mattern,
polynomial, etc). Based on a MATLAB implementation by Neil D. Lawrence.
See inst/doc/index.html for more details.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
