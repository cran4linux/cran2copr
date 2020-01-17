%global packname  eventstream
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Streaming Events and their Early Classification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-tensorA 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-AtmRay 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-changepoint 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-tensorA 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-AtmRay 
Requires:         R-CRAN-dbscan 
Requires:         R-MASS 
Requires:         R-CRAN-changepoint 

%description
Implements event extraction and early classification of events in data
streams in R. It has the functionality to generate 2-dimensional data
streams with events belonging to 2 classes. These events can be extracted
and features computed. The event features extracted from incomplete-events
can be classified using a partial-observations-classifier (Kandanaarachchi
et al. 2018) <doi:10.13140/RG.2.2.10051.25129>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
