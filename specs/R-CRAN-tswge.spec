%global packname  tswge
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Applied Time Series Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-PolynomF 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-waveslim 
BuildRequires:    R-CRAN-astsa 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-PolynomF 
Requires:         R-MASS 
Requires:         R-CRAN-waveslim 
Requires:         R-CRAN-astsa 

%description
Accompanies the text Applied Time Series Analysis with R, 2nd edition by
Woodward, Gray, and Elliott. It is helpful for data analysis and for time
series instruction.

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
