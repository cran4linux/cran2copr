%global packname  wkNNMI
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          A Mutual Information-Weighted k-NN Imputation Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-foreach 

%description
Implementation of an adaptive weighted k-nearest neighbours (wk-NN)
imputation algorithm for clinical register data developed to explicitly
handle missing values of continuous/ordinal/categorical and static/dynamic
features conjointly. For each subject with missing data to be imputed, the
method creates a feature vector constituted by the information collected
over his/her first 'window_size' time units of visits. This vector is used
as sample in a k-nearest neighbours procedure, in order to select, among
the other patients, the ones with the most similar temporal evolution of
the disease over time. An ad hoc similarity metric was implemented for the
sample comparison, capable of handling the different nature of the data,
the presence of multiple missing values and include the cross-information
among features.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
