%global packname  ALSM
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Companion to Applied Linear Statistical Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-CRAN-car 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-SuppDists 
Requires:         R-CRAN-car 

%description
Functions and Data set presented in Applied Linear Statistical Models
Fifth Edition (Chapters 1-9 and 16-25), Michael H. Kutner; Christopher J.
Nachtsheim; John Neter; William Li, 2005. (ISBN-10: 0071122214, ISBN-13:
978-0071122214) that do not exist in R, are gathered in this package. The
whole book will be covered in the next versions.

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
