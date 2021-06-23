%global __brp_check_rpaths %{nil}
%global packname  rccdates
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Date Functions for Swedish Cancer Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rccmisc 
Requires:         R-CRAN-rccmisc 

%description
Identify, convert and handle dates as used within the Swedish cancer
register and associated cancer quality registers in Sweden. Especially the
cancer register sometimes use nonstandard date variables where day and/or
month can be "00" or were the date format is a mixture of"%Y-%m-%d",
"%Y%m%d" and "%y%V" (two digit year and week number according to ISO
8601,which is not completely supported by R).These dates must be
approximated to valid dates before being used in for example survival
analysis. The package also includes some convenient functions for
calculating "lead times" (relying on 'difftime') and introduce a "year"
class with relevant S3-methods to handle yearly cohort.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
