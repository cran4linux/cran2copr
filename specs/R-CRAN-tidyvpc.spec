%global packname  tidyvpc
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          VPC Percentiles and Prediction Intervals

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.51
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
Requires:         R-CRAN-quantreg >= 5.51
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-magrittr 
Requires:         R-methods 

%description
Perform a Visual Predictive Check (VPC), while accounting for
stratification, censoring, and prediction correction. Using piping from
'magrittr', the intuitive syntax gives users a flexible and powerful
method to generate VPCs using both traditional binning and a new binless
approach Jamsen et al. (2018) <doi:10.1002/psp4.12319> with Additive
Quantile Regression (AQR) and Locally Estimated Scatterplot Smoothing
(LOESS) prediction correction.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/plotfunction.R
%doc %{rlibdir}/%{packname}/prepare_vpc.R
%doc %{rlibdir}/%{packname}/vpc_app.r
%{rlibdir}/%{packname}/INDEX
