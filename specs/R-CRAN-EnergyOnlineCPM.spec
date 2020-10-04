%global packname  EnergyOnlineCPM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Distribution Free Multivariate Control Chart Based on EnergyTest

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-energy 
Requires:         R-MASS 

%description
Provides a function for distribution free control chart based on the
change point model, for multivariate statistical process control. The main
constituent of the chart is the energy test that focuses on the
discrepancy between empirical characteristic functions of two random
vectors. This new control chart highlights in three aspects. Firstly, it
is distribution free, requiring no knowledge of the random processes.
Secondly, this control chart can monitor mean and variance simultaneously.
Thirdly it is devised for multivariate time series which is more practical
in real data application. Fourthly, it is designed for online detection
(Phase II), which is central for real time surveillance of stream data.
For more information please refer to O. Okhrin and Y.F. Xu (2017)
<https://github.com/YafeiXu/working_paper/raw/master/CPM102.pdf>.

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
