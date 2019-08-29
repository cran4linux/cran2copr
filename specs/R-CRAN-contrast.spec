%global packname  contrast
%global packver   0.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.21
Release:          1%{?dist}
Summary:          A Collection of Contrast Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.1
Requires:         R-core >= 2.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-rms 
Requires:         R-nlme 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-geepack 
Requires:         R-MASS 
Requires:         R-CRAN-sandwich 

%description
One degree of freedom contrasts for lm, glm, gls, and geese objects.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
