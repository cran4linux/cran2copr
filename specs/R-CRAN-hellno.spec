%global packname  hellno
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Providing 'stringsAsFactors=FALSE' Variants of 'data.frame()'and 'as.data.frame()'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Base R's default setting for 'stringsAsFactors' within 'data.frame()' and
'as.data.frame()' is supposedly the most often complained about piece of
code in the R infrastructure. The 'hellno' package provides an explicit
solution without changing R itself or having to mess around with options.
It tries to solve this problem by providing alternative 'data.frame()' and
'as.data.frame()' functions that are in fact simple wrappers around base
R's 'data.frame()' and 'as.data.frame()' with 'stringsAsFactors' option
set to 'HELLNO' ( which in turn equals FALSE ) by default.

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
%{rlibdir}/%{packname}/INDEX
