%global __brp_check_rpaths %{nil}
%global packname  MethComp
%global packver   1.30.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.30.0
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Agreement in Method Comparison Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-rjags 
Requires:         R-CRAN-coda 
Requires:         R-nlme 
Requires:         R-CRAN-rjags 

%description
Methods (standard and advanced) for analysis of agreement between
measurement methods. These cover Bland-Altman plots, Deming regression,
Lin's Total deviation index, and difference-on-average regression. See
Carstensen B. (2010) "Comparing Clinical Measurement Methods: A Practical
Guide (Statistics in Practice)" <doi:10.1002/9780470683019> for more
information.

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
