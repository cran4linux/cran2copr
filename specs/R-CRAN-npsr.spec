%global __brp_check_rpaths %{nil}
%global packname  npsr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Validate Instrumental Variables using NPS

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-gmp 
Requires:         R-CRAN-infotheo 
Requires:         R-MASS 
Requires:         R-CRAN-gmp 

%description
An R implementation of the Necessary and Probably Sufficient (NPS) test
for finding valid instrumental variables, as suggested by Amit Sharma
(2016, Working Paper)
<http://amitsharma.in/pubs/necessary_probably_sufficient_iv_test.pdf>. The
NPS test, compares the likelihood that a given set of observational data
of the three variables Z, X and Y is generated by a valid instrumental
variable model (Z -> X -> Y) to the likelihood that the data is generated
by an invalid IV model.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
