%global packname  mma
%global packver   10.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          10.0.0
Release:          1%{?dist}
Summary:          Multiple Mediation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-splines 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-lattice 
Requires:         R-CRAN-gbm 
Requires:         R-splines 
Requires:         R-survival 
Requires:         R-CRAN-car 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-plotrix 
Requires:         R-lattice 

%description
Used for general multiple mediation analysis. The analysis method is
described in Yu et al. (2014) <doi:10.4172/2155-6180.1000189> "General
Multiple Mediation Analysis With an Application to Explore Racial
Disparity in Breast Cancer Survival", published on Journal of Biometrics &
Biostatistics, 5(2):189; and Yu et al.(2017)
<DOI:10.1016/j.sste.2017.02.001> "Exploring racial disparity in obesity: a
mediation analysis considering geo-coded environmental factors", published
on Spatial and Spatio-temporal Epidemiology, 21, 13-23.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
