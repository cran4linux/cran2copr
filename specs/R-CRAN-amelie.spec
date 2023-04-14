%global __brp_check_rpaths %{nil}
%global packname  amelie
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Anomaly Detection with Normal Probability Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implements anomaly detection as binary classification for cross-sectional
data. Uses maximum likelihood estimates and normal probability functions
to classify observations as anomalous. The method is presented in the
following lecture from the Machine Learning course by Andrew Ng:
<https://www.coursera.org/learn/machine-learning/lecture/C8IJp/algorithm/>,
and is also described in: Aleksandar Lazarevic, Levent Ertoz, Vipin Kumar,
Aysel Ozgur, Jaideep Srivastava (2003) <doi:10.1137/1.9781611972733.3>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
