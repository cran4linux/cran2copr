%global __brp_check_rpaths %{nil}
%global packname  YaleToolkit
%global packver   4.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Data exploration tools from Yale University.

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
Requires:         R-grid 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 

%description
This collection of data exploration tools was developed at Yale University
for the graphical exploration of complex multivariate data; barcode and
gpairs now have their own packages.  The new big.read.table() provided
here may be useful for large files when only a subset is needed.

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
