%global packname  GENEAclassify
%global packver   1.4.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.18
Release:          3%{?dist}
Summary:          Segmentation and Classification of Accelerometer Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-GENEAread 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-rpart 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-CRAN-GENEAread 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-signal 
Requires:         R-rpart 

%description
Segmentation and classification procedures for data from the
'Activinsights GENEActiv'
<https://www.activinsights.com/products/geneactiv/> accelerometer that
provides the user with a model to guess behaviour from test data where
behaviour is missing. Includes a step counting algorithm, a function to
create segmented data with custom features and a function to use recursive
partitioning provided in the function rpart() of the 'rpart' package to
create classification models.

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
%{rlibdir}/%{packname}/testdata
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
