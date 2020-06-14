%global packname  SurvTrunc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Analysis of Doubly Truncated Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Package performs Cox regression and survival distribution function
estimation when the survival times are subject to double truncation. The
estimation procedure for each method involves inverse probability
weighting, where the weights correspond to the inverse of the selection
probabilities and are estimated using the survival times and truncation
times only. Both methods require that the survival and truncation times
are quasi-independent. A test for checking this independence assumption is
also included in this package. The functions available in this package for
Cox regression, survival distribution function estimation, and testing
independence under double truncation are based on the following methods,
respectively: Rennert and Xie (2017) <doi:10.1111/biom.12809>, Shen (2010)
<doi:10.1007/s10463-008-0192-2>, Martin and Betensky (2005)
<doi:10.1198/016214504000001538>.

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
