%global packname  BatchExperiments
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          2%{?dist}
Summary:          Statistical Experiments on Batch Computing Clusters

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RSQLite >= 2.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-checkmate >= 1.8.5
BuildRequires:    R-CRAN-BatchJobs >= 1.7
BuildRequires:    R-CRAN-BBmisc >= 1.11
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DBI 
Requires:         R-CRAN-RSQLite >= 2.0
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-checkmate >= 1.8.5
Requires:         R-CRAN-BatchJobs >= 1.7
Requires:         R-CRAN-BBmisc >= 1.11
Requires:         R-CRAN-backports 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-DBI 

%description
Extends the BatchJobs package to run statistical experiments on batch
computing clusters. For further details see the project web page.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
