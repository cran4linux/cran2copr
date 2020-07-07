%global packname  sicegar
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}
Summary:          Analysis of Single-Cell Viral Growth Curves

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Aims to quantify time intensity data by using sigmoidal and double
sigmoidal curves. It fits straight lines, sigmoidal, and double sigmoidal
curves on to time vs intensity data. Then all the fits are used to make
decision on which model (sigmoidal, double sigmoidal, no signal or
ambiguous) best describes the data. No signal means the intensity does not
reach a high enough point or does not change at all over time. Sigmoidal
means intensity starts from a small number than climbs to a maximum.
Double sigmoidal means intensity starts from a small number, climbs to a
maximum then starts to decay. After the decision between those four
options, the algorithm gives the sigmoidal (or double sigmoidal)
associated parameter values that quantifies the time intensity curve. The
origin of the package name came from "SIngle CEll Growth Analysis in R".

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
