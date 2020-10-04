%global packname  ADDT
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Accelerated Destructive Degradation Test Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-coneproj 
Requires:         R-nlme 
Requires:         R-Matrix 
Requires:         R-CRAN-coneproj 

%description
Accelerated destructive degradation tests (ADDT) are often used to collect
necessary data for assessing the long-term properties of polymeric
materials. Based on the collected data, a thermal index (TI) is estimated.
The TI can be useful for material rating and comparison. This package
implements the traditional method based on the least-squares method, the
parametric method based on maximum likelihood estimation, and the
semiparametric method based on spline methods, and the corresponding
methods for estimating TI for polymeric materials. The traditional
approach is a two-step approach that is currently used in industrial
standards, while the parametric method is widely used in the statistical
literature. The semiparametric method is newly developed. Both the
parametric and semiparametric approaches allow one to do statistical
inference such as quantifying uncertainties in estimation, hypothesis
testing, and predictions. Publicly available datasets are provided
illustrations. More details can be found in Jin et al. (2017).

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
