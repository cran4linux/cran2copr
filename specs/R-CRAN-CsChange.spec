%global packname  CsChange
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}
Summary:          Testing for Change in C-Statistic

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-survival 
BuildRequires:    R-boot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-rms 
Requires:         R-survival 
Requires:         R-boot 
Requires:         R-stats 
Requires:         R-CRAN-Hmisc 

%description
Calculate the confidence interval and p value for change in C-statistic.
The adjusted C-statistic is calculated by using formula as "Somers' Dxy
rank correlation"/2+0.5. The confidence interval was calculated by using
the bootstrap method. The p value was calculated by using the Z testing
method. Please refer to the article of Peter Ganz et al. (2016)
<doi:10.1001/jama.2016.5951>.

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
%{rlibdir}/%{packname}/INDEX
