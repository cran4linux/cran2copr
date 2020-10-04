%global packname  tfruns
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Training Run Tools for 'TensorFlow'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.2
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-jsonlite >= 1.2
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-utils 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-config 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-reticulate 

%description
Create and manage unique directories for each 'TensorFlow' training run.
Provides a unique, time stamped directory for each run along with
functions to retrieve the directory of the latest run or latest several
runs.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/views
%{rlibdir}/%{packname}/INDEX
