%global packname  PowerTOST
%global packver   1.4-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.9
Release:          3%{?dist}
Summary:          Power and Sample Size for (Bio)Equivalence Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cubature >= 1.3.6
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-tufte 
Requires:         R-CRAN-cubature >= 1.3.6
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-tufte 

%description
Contains functions to calculate power and sample size for various study
designs used in bioequivalence studies. Use known.designs() to see the
designs supported. Power and sample size can be obtained based on
different methods, amongst them prominently the TOST procedure (two
one-sided t-tests). See README and NEWS for further information.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
