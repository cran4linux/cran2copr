%global packname  msme
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}
Summary:          Functions and Datasets for "Methods of Statistical ModelEstimation"

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-lattice 
Requires:         R-MASS 
Requires:         R-lattice 

%description
Functions and datasets from Hilbe, J.M., and Robinson, A.P. 2013. Methods
of Statistical Model Estimation. Chapman & Hall / CRC.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/1-programming.R
%doc %{rlibdir}/%{packname}/2-estimation.R
%doc %{rlibdir}/%{packname}/3-regression.R
%doc %{rlibdir}/%{packname}/4-logistic.R
%doc %{rlibdir}/%{packname}/5-advanced-glm.R
%{rlibdir}/%{packname}/6-panel-data.R
%doc %{rlibdir}/%{packname}/7-bayes.R
%{rlibdir}/%{packname}/INDEX
