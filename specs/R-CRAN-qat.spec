%global packname  qat
%global packver   0.74
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.74
Release:          3%{?dist}
Summary:          Quality Assurance Toolkit

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.1
Requires:         R-core >= 2.6.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-moments 
Requires:         R-boot 
Requires:         R-CRAN-fields 

%description
Functions for a scientific quality assurance of meteorological data.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
