%global packname  TimeWarp
%global packver   1.0.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.15
Release:          3%{?dist}
Summary:          Date Calculations and Manipulation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6
Requires:         R-core >= 2.6
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Date sequence, relative date calculations, and date manipulation with
business days and holidays.  Works with Date and POSIXt classes.

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
%doc %{rlibdir}/%{packname}/sccversion.txt
%doc %{rlibdir}/%{packname}/svnversion.txt
%{rlibdir}/%{packname}/INDEX
