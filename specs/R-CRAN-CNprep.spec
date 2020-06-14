%global packname  CNprep
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          2%{?dist}
Summary:          Pre-process DNA Copy Number (CN) Data for Detection of CN Events

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-rlecuyer 
Requires:         R-parallel 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-rlecuyer 

%description
This package evaluates DNA copy number data, using both their initial form
(copy number as a noisy function of genomic position) and their
approximation by a piecewise-constant function (segmentation), for the
purpose of identifying genomic regions where the copy number differs from
the norm.

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
