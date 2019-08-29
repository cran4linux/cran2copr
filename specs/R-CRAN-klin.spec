%global packname  klin
%global packver   2007-02-05
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2007.02.05
Release:          1%{?dist}
Summary:          Linear equations with Kronecker structure

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-Matrix >= 0.9975.8
Requires:         R-Matrix >= 0.9975.8

%description
The package implements efficient ways to evaluate and solve equations of
the form Ax=b, where A is a kronecker product of matrices.  Functions to
solve least squares problems of this type are also included.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
