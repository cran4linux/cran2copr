%global packname  ui
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Uncertainty Intervals and Sensitivity Analysis for Missing Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-graphics 
Requires:         R-stats 

%description
Implements functions to derive uncertainty intervals for (i) regression
(linear and probit) parameters when outcome is missing not at random
(non-ignorable missingness) introduced in Genbaeck, M., Stanghellini, E.,
de Luna, X. (2015) <doi:10.1007/s00362-014-0610-x> and Genbaeck, M., Ng,
N., Stanghellini, E., de Luna, X. (2018) <doi:10.1007/s10433-017-0448-x>;
and (ii) double robust and outcome regression estimators of average causal
effects (on the treated) with possibly unobserved confounding introduced
in Genbaeck, M., de Luna, X. (2018) <doi:10.1111/biom.13001>.

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
